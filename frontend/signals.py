from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from db.models import User, FriendRequest


@receiver(post_save, sender=FriendRequest)
def post_save_add_to_friend(sender, instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    if instance.status == 'accepted':
        sender.friends.add(receiver)
        receiver.friends.add(sender)
        sender.save()
        receiver.save()


@receiver(pre_delete, sender=FriendRequest)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    sender.friends.remove(receiver)
    receiver.friends.remove(sender)
    sender.save()
    receiver.save()
