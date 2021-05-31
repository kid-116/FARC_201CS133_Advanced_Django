from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'lectures'

urlpatterns = [
    url('create/', views.create, name='create_path'),
    path('<int:id_l>/edit/', views.edit, name='edit_path'),
]