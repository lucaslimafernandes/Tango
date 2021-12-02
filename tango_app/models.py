#from django.conf import settings
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

"""class User_profile(models.Model):
    user_id = 'USER'
    user_profile = models.CharField(max_length=20)
"""

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    dt_init = models.DateTimeField()
    dt_conclusion = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=30)
    priority = models.CharField(max_length=12, blank=True, null=True)
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Task_responses(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_response = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user_response = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_response = models.DateTimeField()
    status = models.CharField(max_length=30)
    description_response = models.TextField()

#https://stackoverflow.com/questions/34305805/foreignkey-user-in-models
#https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model

"""
class User_role(models.Model):
    user_role = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    status_role = models.CharField(max_length=12)
    dt_init_role = models.DateTimeField()
    dt_end_role = models.DateTimeField(blank=True, null=True)
"""