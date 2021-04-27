from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from accounts.models import *


def normal_user_create_profile(sender,instance,created, **kwargs):
    if created:
            group= Group.objects.get(name="Normal_Users")
            instance.groups.add(group)
            Normal_Users.objects.create(
                user = instance,    
                First_Name = instance.first_name

            )
            print('User Profile Done')


post_save.connect(normal_user_create_profile,sender =User)