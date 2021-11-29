from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('home/', views.logged, name='logged'),
    path('list/', views.task_list, name='task_list'),
    path('newtask', views.criar_task, name='criar_task'),
    path('list/<int:pk>/', views.view_task, name='view_task'),
    path('add_action/<int:pk>/', views.view_task_add_action, name='task_add_action'),
    path('new_user/', views.new_user, name='new_user'),
    path('che/', views.che, name='che'),
]

#Pagina de cadastro de usuários
#https://ohmycode.com.br/cadastro-e-autenticacao-de-usuarios-no-django/