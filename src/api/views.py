from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from applicant.models import SlovakiaApplicant, SlovakiaProcess, BRTAApplicant, DateOpen
from country.models import Country, Center
from proxy.models import Authenticated_Proxy


# -------------------- Slovakia ---------------------
def slovakia_applicants(request):
    return JsonResponse({
        'fake': len(SlovakiaApplicant.objects.filter(applicant_type='fake')),
        'original': len(SlovakiaApplicant.objects.filter(applicant_type='original'))
    })


def slovakia_applicant(request, applicant_type):
    data = {}
    if applicant_type == 'fake':
        applicant = SlovakiaApplicant.objects.filter(applicant_type=applicant_type).first()
        if applicant:
            data = {
                'username': applicant.username,
                'passport': applicant.passport
            }
            applicant.delete()
    else:
        applicant = SlovakiaApplicant.objects.filter(applicant_type=applicant_type, date_reserved=False, taken=False).first()
        if applicant:
            data = {
                'username': applicant.username,
                'passport': applicant.passport,
                'applicant_id': applicant.id
            }
    return JsonResponse(data)


def slovakia_date_open(request):
    country = Country.objects.filter(name='Slovakia').first()
    open_dates = DateOpen.objects.filter(country=country)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    data = [f'Date is now avail at {months[open_date.month-1]}, {open_date.center.name}.' for open_date in open_dates if open_date.date_open]
    return JsonResponse({
        'centers': data
    })


def slovakia_date_open_status(request, center_code, month):
    country = Country.objects.filter(name='Slovakia').first()
    center = Center.objects.filter(code=center_code).first()
    date_instance = DateOpen.objects.filter(country=country, center=center, month=month).first()
    date_instance.date_open = True
    date_instance.save()
    return JsonResponse({
        'success': True
    })


def slovakia_process_status_change(request, process_id):
    process = SlovakiaProcess.objects.get(pk=process_id)
    if process:
        process.status = not process.status
        process.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def slovakia_processes(request):
    processes = SlovakiaProcess.objects.all()
    data = []
    for process in processes:
        data.append({
            'process_id': process.id,
            'center_code': process.center.code,
            'status': process.status,
            'month': process.month,
            'process_type': process.process_type
        })
    return JsonResponse({'processes': data})


# ---------------------- BRTA -----------------------
def brta_applicants(request):
    return JsonResponse({
        'fake': len(BRTAApplicant.objects.filter(applicant_type='fake')),
        'original': len(BRTAApplicant.objects.filter(applicant_type='original'))
    })


def brta_applicant(request):
    applicant = BRTAApplicant.objects.filter(applicant_type='original', date_reserved=False, taken=False).first()
    return JsonResponse({
        'username': applicant.username,
        'passport': applicant.password,
        'applicant_id': applicant.id
    })


def brta_date_open(request):
    country = Country.objects.filter(name='BRTA').first()
    open_dates = DateOpen.objects.filter(country=country)
    data = [f'Date is now avail at {open_date.center.name}.' for open_date in open_dates]
    return JsonResponse({
        'centers': data
    })


# ---------------------- Proxy -------------------------
def authenticated_proxy(request, country):
    proxy = Authenticated_Proxy.objects.filter(country=country).first()
    data = {}
    if proxy:
        data = {
            'address': proxy.address,
            'port': proxy.port,
            'username': proxy.username,
            'password': proxy.password
        }
    return JsonResponse(data)
