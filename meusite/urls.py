from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/<int:pk>', views.anime, name='anime'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contatos/', views.contatos, name='contatos'),
    path('sobre/', views.sobre, name='sobre'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('delete/<int:pk>', views.delete, name='delete'),
]