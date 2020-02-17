from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('country/', include('country.urls')),
    path('applicant/', include('applicant.urls')),
    path('proxy/', include('proxy.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
