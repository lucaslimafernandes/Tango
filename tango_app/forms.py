from django import forms
from django.db.models import fields
from .models import Task, Task_responses
from django.contrib.auth.models import User

#Validação HTML
class form_criarTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority')

class form_newUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name','email','first_name')

#Validação salvar no DB
class criarTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class criarTaskResponse(forms.ModelForm):
    class Meta:
        model = Task_responses
        fields = '__all__'