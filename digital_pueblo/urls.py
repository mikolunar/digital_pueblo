"""digital_pueblo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from anuncios import views as anuncios_views
from blog import views as blog_views
from users import views as user_views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/anuncios/', anuncios_views.AnunciosListAPI.as_view(),
         name='anuncios_list_api'),
    path('anuncios/', anuncios_views.anunciosView, name='anuncios'),
    path('api/anuncio/<int:pk>/', anuncios_views.AnunciosDetailsAPI.as_view(),
         name='anuncio_details'),
    path('anuncio/<int:pk>/', anuncios_views.anuncioView, name='anuncio_view'),
    path('anuncio_rem/<int:pk>', anuncios_views.anuncioRem, name='anuncio_rem'),
    path('anuncio_del/<int:pk>', anuncios_views.anuncioDel, name='anuncio_del'),
    path('anuncio_edit/<int:pk>', anuncios_views.anuncioEdit, name='anuncio_edit'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('blog/', TemplateView.as_view(template_name='blog/blog.html'), name='blog_home'),
    path('anuncio_new/', anuncios_views.anuncioNew,
         name='anuncio_new'),
    path('api/anuncios/', TemplateView.as_view(template_name='blog/blog.html'),
         name='anuncios_api'),
    path('contact/', TemplateView.as_view(template_name='blog/blog.html'), name='contact'),
    path('register/', user_views.register, name='register')
]
