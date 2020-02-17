from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Free_Proxy, Authenticated_Proxy
from country.models import Country


def home(request):
    context = {
        'free_proxy': Free_Proxy.objects.all(),
        'free_proxy_used': Free_Proxy.objects.filter(taken=False),
        'authenticated_proxy': Authenticated_Proxy.objects.all()
    }
    return render(request, 'proxy/home.html', context)


def add_free_proxy(request):
    if request.method == 'POST':
        if request.FILES:
            file = request.FILES['file']
            counter = 0
            for chunk in file.chunks():
                for line in chunk.splitlines():
                    line = str(line).replace('\'', '').replace('b', '')
                    line = line.split(':')
                    if not Free_Proxy.objects.filter(address=line[0], port=line[1]).first():
                        new_proxy = Free_Proxy(address=line[0], port=line[1])
                        new_proxy.save()
                        counter += 1
    messages.success(request, f'{counter} new free proxy has been added.')
    return redirect('proxy-list')


def delete_free_proxy(request):
    proxies = Free_Proxy.objects.all()
    for proxy in proxies:
        proxy.delete()
    messages.success(request, f'All free proxy has been deleted.')
    return redirect('proxy-list')


def add_authenticated_proxy(request):
    if request.method == 'POST':
        if request.FILES:
            file = request.FILES['file']
            counter = 0
            for chunk in file.chunks():
                for line in chunk.splitlines():
                    line = str(line).replace('\'', '').replace('b', '')
                    line = line.split(':')
                    address = line[0]
                    port = line[1]
                    username = line[2]
                    password = line[3]
                    country = line[4]
                    proxy = Authenticated_Proxy.objects.filter(address=address, port=port, username=username).first()
                    if not proxy:
                        new_proxy = Authenticated_Proxy(address=address, port=port, username=username, password=password, country=country)
                        new_proxy.save()
                        counter += 1
    messages.success(request, f'{counter} new authenticated proxy has been added.')
    return redirect('proxy-list')


def delete_authenticated_proxy(request):
    proxies = Authenticated_Proxy.objects.all()
    for proxy in proxies:
        proxy.delete()
    messages.success(request, f'All authenticated proxy has been deleted.')
    return redirect('proxy-list')
