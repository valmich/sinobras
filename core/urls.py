from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ControleQualidade/', include('ControleQualidade.urls')),  # Inclui as URLs do app ''
  
]