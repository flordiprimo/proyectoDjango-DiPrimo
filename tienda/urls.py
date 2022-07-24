from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='inicio'),
    path('login', login_request , name='login'),
    path('register', register_request , name='register'),
    path('logout', logout_request , name='logout'),
    path('editar-perfil', editar_perfil , name='editar_perfil'),
    path('cambiar-password', PasswordResetByUser.as_view() , name='cambiar_password'),
    path('agregar-avatar', agregar_avatar , name='agregar_avatar'),
    path('mi-perfil', mi_perfil , name='mi_perfil'),
    path('editar-productos', editarProductos , name='editar_productos'),
    path('about', about , name='about'),
    
    path('remeras/', remeras, name='remeras'),
    path('pantalones/', pantalones, name='pantalones'),
    path('camisas/', camisas, name='camisas'),
    path('buscar-remera/', buscarRemera, name='buscar-remera'),
    path('buscar-pantalon/', buscarPantalon, name='buscar-pantalon'),
    path('buscar-camisa/', buscarCamisa, name='buscar-camisa'),

    path('remera/list', RemerasList.as_view() , name='remera_list'),
    path('remera_detalle/<pk>', RemeraDetail.as_view() , name='remera_detail'),
    path('remera_formulario/', RemeraCreate.as_view() , name='remera_create'),
    path('remera_formulario/<pk>', RemeraUpdate.as_view() , name='remera_update'),
    path('remera_eliminar/<pk>', RemeraDelete.as_view() , name='remera_delete'),
    
    path('camisa/list', CamisasList.as_view() , name='camisa_list'),
    path('camisa_detalle/<pk>', CamisaDetail.as_view() , name='camisa_detail'),
    path('camisa_formulario/', CamisaCreate.as_view() , name='camisa_create'),
    path('camisa_formulario/<pk>', CamisaUpdate.as_view() , name='camisa_update'),
    path('camisa_eliminar/<pk>', CamisaDelete.as_view() , name='camisa_delete'),
    
    path('pantalon/list', PantalonesList.as_view() , name='pantalon_list'),
    path('pantalon_detalle/<pk>', PantalonDetail.as_view() , name='pantalon_detail'),
    path('pantalon_formulario/', PantalonCreate.as_view() , name='pantalon_create'),
    path('pantalon_formulario/<pk>', PantalonUpdate.as_view() , name='pantalon_update'),
    path('pantalon_eliminar/<pk>', PantalonDelete.as_view() , name='pantalon_delete'),
    


]