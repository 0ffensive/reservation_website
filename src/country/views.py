from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Country, Center
from .forms import CountryForm, CenterForm


def country_list(request):
    context = {
        'countries': Country.objects.all(),
        'centers': Center.objects.all()
    }
    return render(request, 'country/list.html', context)


def country_add(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            Country.objects.create(**form.cleaned_data)
            messages.success(request, 'Succfully added a new country.')
        else:
            print(form.errors)
            messages.error(request, 'Invalid information in the form.')
    return redirect('country-list')


def country_update(request, country_id):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country = Country.objects.get(pk=country_id)
            if country:
                country.name = form.cleaned_data.get('name')
                country.url = form.cleaned_data.get('url')
                country.save()
                messages.success(request, 'Successfully updated.')
            else:
                messages.error(request, 'The country does not exist.')
        else:
            messages.error(request, 'Invalid information in the form.')
    return redirect('country-list')


def country_delete(request, country_id):
    country = Country.objects.get(pk=country_id)
    if country:
        country.delete()
        messages.success(request, 'Successfully deleted the country.')
    else:
        messages.error(request, 'The country does not exist.')
    return redirect('country-list')


def center_add(request, country_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name', None),
            'code': request.POST.get('code', None),
            'country': country_id
        }
        form = CenterForm(data=data)
        if form.is_valid():
            form.cleaned_data['country'] = Country.objects.get(pk=form.cleaned_data.get('country'))
            Center.objects.create(**form.cleaned_data)
            messages.success(request, 'Succfully added a new center.')
        else:
            print(form.errors)
            messages.error(request, 'Invalid information in the form.', extra_tags='danger')
    return redirect('country-list')


def center_update(request, country_id, center_id):
    pass


def center_delete(request, country_id, center_id):
    center = Center.objects.get(pk=center_id)
    if center:
        center.delete()
    return redirect('country-list')
