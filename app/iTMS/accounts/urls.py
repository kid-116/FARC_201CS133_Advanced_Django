from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url('signup/', views.signup_acc, name='signup_path'),
    url('logout/', views.logout_acc, name='logout_path'),
    url('login/', views.login_acc, name='login_path'),
]