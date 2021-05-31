from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    url('create/', views.create, name='create_path'),
    path('<int:id_e>/edit/', views.edit, name='edit_path'),
    path('<int:id_e>/delete/', views.delete, name='delete_path')
]