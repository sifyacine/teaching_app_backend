from .models import CreateChannel
def increase_likes(channel_id):
    try:
        channel = CreateChannel.objects.get(id=channel_id)
        channel.channel_likes += 1
        channel.save()
        return True
    except CreateChannel.DoesNotExist:
        return False
