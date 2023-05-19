from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import index, contacto

urlpatterns = [
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
