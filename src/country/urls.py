from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.country_add, name='country-add'),
    path('list/', views.country_list, name='country-list'),
    path('<int:country_id>/update/', views.country_update, name='country-update'),
    path('<int:country_id>/delete/', views.country_delete, name='country-delete'),
    path('<int:country_id>/center/add/', views.center_add, name='center-add'),
    path('<int:country_id>/center/<int:center_id>/update/', views.center_update, name='center-edit'),
    path('<int:country_id>/center/<int:center_id>/delete/', views.center_delete, name='center-delete'),
]
