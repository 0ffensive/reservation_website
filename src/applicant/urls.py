from django.urls import path
from . import views

urlpatterns = [
    path('poland/', views.poland, name='applicant-poland'),
    # Slovakia
    path('slovakia/', views.slovakia, name='applicant-slovakia'),
    path('slovakia/add-applicant/', views.slovakia_add_applicant, name='applicant-slovakia-add'),
    path('slovakia/<int:id>/edit-applicant/', views.slovakia_edit_applicant, name='applicant-slovakia-edit'),
    path('slovakia/<int:id>/delete-applicant/', views.slovakia_delete_applicant, name='applicant-slovakia-delete'),
    path('slovakia/process/add/', views.slovakia_add_process, name='applicant-slovakia-process-add'),
    path('slovakia/process/<int:process_id>/delete/', views.slovakia_delete_process, name='applicant-slovakia-process-delete'),
    # BRTA
    path('brta/', views.brta, name='applicant-brta'),
    path('brta/add-applicant/', views.brta_add_applicant, name='applicant-brta-add'),
    path('brta/<int:id>/edit-applicant/', views.brta_edit_applicant, name='applicant-brta-edit'),
    path('brta/<int:id>/delete-applicant/', views.brta_delete_applicant, name='applicant-brta-delete'),
]
