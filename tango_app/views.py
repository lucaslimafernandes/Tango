from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.db.models import Count
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task, Task_responses
from django.contrib.auth.models import User
from .forms import criarTaskResponse, form_criarTask, criarTask, form_newUser
from datetime import date, datetime
from django.contrib.auth.hashers import make_password

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Tango:logged'))
            else:
                # Retorna uma mensagem de erro de conta desabilitada
                return render(request, 'tango_app/login_page.html', {'msgLogin': 'erro'})
        else:
            # Retorna uma mensagem de erro login inválido
            return render(request, 'tango_app/login_page.html', {'msgLogin': 'invalido'})
    else:
        return render(request, 'tango_app/login_page.html')


@login_required
def logged(request):
    return render(request, 'tango_app/index_logged.html')


def new_user(request):
    if request.method == 'POST':
        form = form_newUser(request.POST)
        if form.is_valid():

            
            user_aux = User.objects.filter(email=request.POST.get('email')).count()
            if user_aux >= 1:
                return render(request, 'tango_app/new_user.html', {'err':'email1'})

            else:
        
                usernam = request.POST.get('first_name').lower() + '.' + request.POST.get('last_name')[0:3].lower()
                first_nam = request.POST.get('first_name')
                last_nam = request.POST.get('last_name')
                emai = request.POST.get('email')
                passwor = make_password(request.POST.get('password'))
                # erro no passwd


                newUser = User.objects.create_user(username=usernam, first_name=first_nam, last_name=last_nam, email=emai, password=passwor)

                newUser.save()
                
                return render(request, 'tango_app/registered_new_user.html', {
                                                                            'username':usernam,
                                                                            'first_name':first_nam,
                                                                            'last_name':last_nam,
                                                                            'email':emai
                                                                            })
                #return redirect(reverse('Tango:login_page'))

    else:
        return render(request, 'tango_app/new_user.html') 


def che(request):
    
    usuario = request.user
    #usuario_role = User_role.objects.filter(user_role=usuario).values()
    #usuario_role = get_object_or_404(User_role, user_role=usuario)
    return HttpResponse(usuario.is_staff)


@login_required
def task_list(request):

    #criar filtro por usuário

    usuario = request.user

    if usuario.is_staff:

        tasks = Task.objects.all()
        content = {'tasks':tasks, 'solver':'True'}
        return render(request, 'tango_app/task_list.html', content)

    else:
        tasks = Task.objects.filter(user_owner=usuario)
        content = {'tasks':tasks}
        return render(request, 'tango_app/task_list.html', content)


@login_required
def criar_task(request):
    if request.method == 'POST':

        #form django de validação do HTML
        form = form_criarTask(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            desc = request.POST.get('description')
            context = {
                'dt_init': datetime.now(),
                'status':'STARTED', 
                'title':title, 
                'description': desc,
                'priority': request.POST.get('priority'),
                'user_owner': request.user.pk
                }

            form_save = criarTask(context)
            if form_save.is_valid():
                new_form = form_save.save()

                #task_ = Task.objects.filter
                #https://stackoverflow.com/questions/732952/get-primary-key-after-saving-a-modelform-in-django/732973

                #return HttpResponse(new.id)
                context = {
                    'task':new_form.id,
                    'user_response': request.user.pk,
                    'dt_response': datetime.now(),
                    'status': 'OWNER',
                    'description_response': 'Registro inicial'
                }
                form_responses = criarTaskResponse(context)
                if form_responses.is_valid():
                    form_responses.save()

                return redirect(reverse('Tango:task_list'))    
                
                #return HttpResponse(context.items())

    
    else:
        return render(request, 'tango_app/criar_task.html',)

@login_required
def view_task(request, pk):
    item = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':

        context = {
                    'task':pk,
                    'user_response': request.user.pk,
                    'dt_response': datetime.now(),
                    'status': 'RESPONSE',
                    'description_response': request.POST.get('response')
                }
        
        item.status = 'RESPONSES'
        item.save()
        
        if request.POST.get('encerrar'):
            context['status'] = 'CLOSING'

            item.status = 'CLOSED'
            item.dt_conclusion = datetime.now()
            item.save()
        
        form = criarTaskResponse(context)
        if form.is_valid():
            form.save()
        
        return redirect(reverse('Tango:task_list'))

    else:

        responses = Task_responses.objects.filter(task_id=item.id)

        return render(request, 'tango_app/view_task.html', {'c':item, 'responses':responses})


@login_required
def view_task_add_action(request, pk):
    return HttpResponse(pk)