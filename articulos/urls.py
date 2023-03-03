from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name="Articulos"

urlpatterns = [
    path('admin/listado/', views.Listado.as_view(), name="listado"),
    path('admin/importar/', views.Importar, name="importar"),
    path('admin/qr/', views.qr_menu, name="qr"),
    path('admin/editar/<int:pk>/', views.Editar.as_view(), name="editar"),
    path('admin/borrar/<int:pk>/', views.Importar, name="borrar"),
    path('admin/ver_menu/<int:pk>/', views.ver_menu, name="ver_menu")

    # path('admin/nuevo/<int:pk>/', views.NuevoProducto.as_view(), name="admin_nuevo_producto"),
    #path('admin/nuevo/', views.NuevaNoticia.as_view(), name="admin_nueva_noticia"),
    #path('admin/editar/<int:pk>/', views.EditarNoticias.as_view(), name="editar"),
    #path('admin/leer/<int:pk>/', views.LeerNoticias, name="leer"),
    #path('admin/eliminar/<int:pk>', views.EliminarNoticias.as_view(), name='eliminar'),
    #path('me-gusta/<int:id_producto>/', views.dar_me_gusta, name="dar_me_gusta")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
