from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='proxy-list'),
    path('add/free-proxy/', views.add_free_proxy, name='proxy-add-free'),
    path('delete/free-proxy/', views.delete_free_proxy, name="proxy-delete-free"),
    path('add/authenticated-proxy/', views.add_authenticated_proxy, name='proxy-add-authenticated'),
    path('delete/authenticated-proxy/', views.delete_authenticated_proxy, name="proxy-delete-authenticated"),
]
