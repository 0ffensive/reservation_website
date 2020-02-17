from django.urls import path
from . import views


urlpatterns = [
    # Applicants: Slovakia
    path('applicants/slovakia/', views.slovakia_applicants),
    path('applicants/slovakia/<str:applicant_type>/applicant/', views.slovakia_applicant),
    path('applicants/slovakia/date-open/', views.slovakia_date_open),
    path('applicants/slovakia/date-open/<int:center_code>/<int:month>/status/', views.slovakia_date_open_status),
    # Applicants: BRTA
    path('applicants/brta/', views.brta_applicants),
    path('applicants/brta/applicant/', views.brta_applicant),
    path('applicants/brta/date-open/', views.brta_date_open),
    # Process: Slovakia
    path('slovakia/processes/', views.slovakia_processes),
    path('process/slovakia/<int:process_id>/status/', views.slovakia_process_status_change),
    # Proxy
    path('<str:country>/authenticated-proxy/', views.authenticated_proxy)
]
