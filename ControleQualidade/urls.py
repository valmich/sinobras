from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views  # Importe as views

urlpatterns = [
    path('', views.home, name='home'),
    path('lotes/', views.lista_lotes, name='lista_lotes'),
    path('lote/avaliar/<str:numero_lote>/', views.avaliar_lote_view, name='avaliar_lote'),
    path('lotes/novo/', views.criar_lote, name='criar_lote'),
    path('lotes/editar/<int:id>/', views.editar_lote, name='editar_lote'),
    path('lotes/deletar/<int:id>/', views.deletar_lote, name='deletar_lote'),
    path('ensaio/', views.criar_ensaio, name='criar_ensaio'),
    #path('ensaios/', views.lista_ensaios, name='lista_ensaios'),
   # path('ensaios/<int:id>/', views.detalhes_ensaio, name='detalhes_ensaio'),
    path('ensaios/editar/<int:id>/', views.editar_ensaio, name='editar_ensaio'),
    path('ensaios/deletar/<int:id>/', views.deletar_ensaio, name='deletar_ensaio'),
    path('caracteristicas/', views.lista_caracteristicas, name='lista_caracteristicas'),
    path('logout/', LogoutView.as_view(next_page='nome_da_url_home'), name='logout'),
]