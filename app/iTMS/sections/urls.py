from django.conf.urls import url
from . import views

app_name = 'sections'

urlpatterns = [
    url('home/', views.home, name='home_path'),
]