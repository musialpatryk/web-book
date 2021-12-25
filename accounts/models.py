from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default='None')
    phone = models.CharField(max_length=50, default='None')
    image = models.ImageField(default='profile_images/UserDefault.png',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username}-Profile'


# Add user to default group during social login
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='viewer'))


def get_users(groupname):
    users = User.objects.filter(groups__name=groupname)
    list = [""]

    for user in users:
        list.append(user.email)

    return list
