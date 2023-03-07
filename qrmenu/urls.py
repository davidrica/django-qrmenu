
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),

    path('', views.inicio, name="inicio"),
    path('modelo2', views.inicio2, name="inicio2"),
    path('modelo3', views.inicio3, name="inicio3"),
    path('articulos/', include('articulos.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
