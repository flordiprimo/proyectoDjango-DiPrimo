from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('remeras/', views.remeras, name='remeras'),
    path('pantalones/', views.pantalones, name='pantalones'),
    path('camisas/', views.camisas, name='camisas'),
    path('crear-remera/', views.crearRemera, name='crear-remera'),
    path('crear-pantalon/', views.crearPantalon, name='crear-pantalon'),
    path('crear-camisa/', views.crearCamisa, name='crear-camisa'),
    path('buscar-remera/', views.buscarRemera, name='buscar-remera'),
    path('buscar-pantalon/', views.buscarPantalon, name='buscar-pantalon'),
    path('buscar-camisa/', views.buscarCamisa, name='buscar-camisa'),
]