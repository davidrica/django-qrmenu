
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),

    path('', views.inicio, name="inicio"),
    path('articulos/', include('articulos.urls')),

]
