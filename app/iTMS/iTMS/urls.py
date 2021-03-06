from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing_path'),
    path('accounts/', include('accounts.urls')),
    path('sections/', include('sections.urls')),
    path('lectures/', include('lectures.urls')),
    path('events/', include('events.urls')),
]
