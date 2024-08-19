from django.urls import path
from .views import (
    group_list_create, group_detail, add_member, approve_membership,  # Updated this line
    send_message, upload_file, upload_image, share_link, group_messages,
    group_files, group_images, group_links, user_groups, suggested_groups,
    request_membership, join_group  # Added these lines
)

urlpatterns = [
    path('groups/', group_list_create, name='group-list-create'),
    path('groups/<int:pk>/', group_detail, name='group-detail'),
    path('groups/<int:pk>/add-member/', add_member, name='add-member'),
    path('groups/<int:pk>/approve-membership/', approve_membership, name='approve-membership'),  # Updated this line
    path('groups/<int:pk>/send-message/', send_message, name='send-message'),
    path('groups/<int:pk>/upload-file/', upload_file, name='upload-file'),
    path('groups/<int:pk>/upload-image/', upload_image, name='upload-image'),
    path('groups/<int:pk>/share-link/', share_link, name='share-link'),
    path('groups/<int:pk>/messages/', group_messages, name='group-messages'),
    path('groups/<int:pk>/files/', group_files, name='group-files'),
    path('groups/<int:pk>/images/', group_images, name='group-images'),
    path('groups/<int:pk>/links/', group_links, name='group-links'),
    path('groups/<int:pk>/request-membership/', request_membership, name='request-membership'),  # Added this line
    path('groups/<int:pk>/join-group/', join_group, name='join-group'),  # Added this line
    path('user-groups/', user_groups, name='user-groups'),
    path('suggested-groups/', suggested_groups, name='suggested-groups'),
]