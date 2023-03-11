
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
    
    
    
    path('modelo2/<int:empresa>/<int:sucursal>/', views.inicio2, name="inicio2"),
        
        
    path('', views.inicio, name="inicio"),
    #path('modelo2', views.inicio2, name="inicio2"),
    #path('modelo3', views.inicio3, name="inicio3"),
    path('articulos/', include('articulos.urls')),
    #sucursales!!!
    path('sucursales/', include('sucursales.urls')),
#usuarios
    path('usuarios/', include('usuarios.urls')),
    
    #passwords
    path(
        "password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='usuarios/password_reset_form.html',), name="password_reset"),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name='usuarios/password_reset_done.html'),name="password_reset_done"),


    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='usuarios/password_reset_confirm.html'),name="password_reset_confirm",),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/password_reset_complete.html'),
        name="password_reset_complete",
    ),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
