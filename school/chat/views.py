from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Group, GroupMembership, Message, File, Image, Link
from .serializers import (
    GroupSerializer, GroupMembershipSerializer, MessageSerializer,
    FileSerializer, ImageSerializer, LinkSerializer
)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Automatically add the admin to the GroupMembership when a group is created
@receiver(post_save, sender=Group)
def add_admin_to_group_membership(sender, instance, created, **kwargs):
    if created:
        GroupMembership.objects.create(user=instance.admin, group=instance, approved=True)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_group(request, pk):
    user = request.user
    group = get_object_or_404(Group, pk=pk)

    # Check if the user is already a member
    if group.members.filter(id=user.id).exists():
        return Response({"detail": "User is already a member of the group."}, status=status.HTTP_400_BAD_REQUEST)

    if group.is_private:
        # Create a pending membership request
        GroupMembership.objects.create(user=user, group=group, approved=False)
        return Response({"detail": "Membership request sent. Awaiting admin approval."}, status=status.HTTP_201_CREATED)
    else:
        # Automatically approve membership for non-private groups
        GroupMembership.objects.create(user=user, group=group, approved=True)
        return Response({"detail": "User joined the group successfully."}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_membership(request, pk):
    user = request.user
    group = get_object_or_404(Group, pk=pk)

    # Check if the user is already a member
    if group.members.filter(id=user.id).exists():
        return Response({"detail": "User is already a member of the group."}, status=status.HTTP_400_BAD_REQUEST)

    if not group.is_private:
        return Response({"detail": "Group is public. Join directly instead of requesting membership."}, status=status.HTTP_400_BAD_REQUEST)

    # Create a pending membership request
    GroupMembership.objects.create(user=user, group=group, approved=False)
    return Response({"detail": "Membership request sent. Awaiting admin approval."}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def group_list_create(request):
    user = request.user

    if request.method == 'GET':
        memberships = GroupMembership.objects.filter(user=user, approved=True)
        groups = Group.objects.filter(
            id__in=memberships.values('group_id')
        ) | Group.objects.filter(admin=user).distinct()
        serializer = GroupSerializer(groups, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        # Ensure request is passed in context
        serializer = GroupSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # Call save without additional admin=user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if group.admin != request.user:
            return Response({"detail": "You do not have permission to edit this group."}, status=status.HTTP_403_FORBIDDEN)
        serializer = GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if group.admin != request.user:
            return Response({"detail": "You do not have permission to delete this group."}, status=status.HTTP_403_FORBIDDEN)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_member(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if group.admin != request.user:
        return Response({"detail": "You do not have permission to add members."}, status=status.HTTP_403_FORBIDDEN)
    user_id = request.data.get('user_id')
    user = get_object_or_404(settings.AUTH_USER_MODEL, pk=user_id)

    if group.members.filter(id=user.id).exists():
        return Response({"detail": "User already a member of the group."}, status=status.HTTP_400_BAD_REQUEST)

    GroupMembership.objects.create(user=user, group=group, approved=False)
    return Response({"detail": "Membership request sent."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_membership(request, pk):
    user = request.user
    group = get_object_or_404(Group, pk=pk)

    if group.admin != user:
        return Response({"detail": "Only the group admin can approve membership requests."}, status=status.HTTP_403_FORBIDDEN)
    
    user_id = request.data.get('user_id')
    membership = get_object_or_404(GroupMembership, user_id=user_id, group=group, approved=False)

    membership.approved = True
    membership.save()
    return Response({"detail": "Membership approved."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request, pk):
    group = get_object_or_404(Group, pk=pk)
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user, group=group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_file(request, pk):
    group = get_object_or_404(Group, pk=pk)
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user, group=group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_image(request, pk):
    group = get_object_or_404(Group, pk=pk)
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user, group=group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def share_link(request, pk):
    group = get_object_or_404(Group, pk=pk)
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user, group=group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def group_messages(request, pk):
    group = get_object_or_404(Group, pk=pk)
    messages = Message.objects.filter(group=group)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def group_files(request, pk):
    group = get_object_or_404(Group, pk=pk)
    files = File.objects.filter(group=group)
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def group_images(request, pk):
    group = get_object_or_404(Group, pk=pk)
    images = Image.objects.filter(group=group)
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def group_links(request, pk):
    group = get_object_or_404(Group, pk=pk)
    links = Link.objects.filter(group=group)
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_groups(request):
    user = request.user
    memberships = GroupMembership.objects.filter(user=user, approved=True)
    groups = Group.objects.filter(id__in=memberships.values('group_id')) | Group.objects.filter(admin=user)

    serializer = GroupSerializer(groups.distinct(), many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def suggested_groups(request):
    user = request.user

    user_group_ids = set(GroupMembership.objects.filter(user=user, approved=True).values_list('group_id', flat=True))
    user_group_ids |= set(Group.objects.filter(admin=user).values_list('id', flat=True))

    suggested_groups = Group.objects.exclude(id__in=user_group_ids)

    serializer = GroupSerializer(suggested_groups, many=True, context={'request': request})
    return Response(serializer.data)