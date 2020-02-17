from django.contrib import admin
from .models import Country, Center


# admin.site.register(Country)
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	search_fields = ['name', 'url']
	list_display = ['name', 'url']


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
	search_fields = ['country', 'name', 'code']
	list_display = ['country', 'name', 'code']
