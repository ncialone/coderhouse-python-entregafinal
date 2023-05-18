from django.contrib import admin
from django.urls import path

from core.views import index, contacto

urlpatterns = [
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('admin/', admin.site.urls),
]
