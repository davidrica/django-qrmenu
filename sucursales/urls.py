from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name="Sucursales"

urlpatterns = [
    path('admin/listado/', views.Listado.as_view(), name="listado"),
    path('admin/editar/<int:pk>/', views.Editar.as_view(), name="editar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
