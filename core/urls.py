from django.urls import path
from . import views
#recordar el nombre de esta app para poder agregarlo a urls del proyecto principal
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
]