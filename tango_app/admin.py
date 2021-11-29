# Register your models here.

from django.contrib import admin
from .models import Task, Task_responses, User

admin.site.register([Task, Task_responses])