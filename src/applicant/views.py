from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SlovakiaApplicant, BRTAApplicant, SlovakiaProcess, DateOpen
from .forms import SlovakiaApplicantForm, BRTAApplicantForm
from country.models import Country, Center


def poland(request):
    return render(request, 'applicant/poland/home.html')


# --------------------------- Slovakia -------------------------------------
def slovakia(request):
    country = Country.objects.filter(name='Slovakia').first()
    centers = Center.objects.filter(country=country)
    context = {
        'fake_applicants': SlovakiaApplicant.objects.filter(applicant_type='fake'),
        'original_applicants': SlovakiaApplicant.objects.filter(applicant_type='original'),
        'centers': centers,
        'processes': SlovakiaProcess.objects.all()
    }
    return render(request, 'applicant/slovakia/home.html', context)


def slovakia_add_applicant(request):
    if request.method == 'POST':
        applicant_type = request.POST.get('applicant_type')
        if applicant_type == 'fake':
            if request.FILES:
                file = request.FILES['file']
                counter = 0
                for chunk in file.chunks():
                    for line in chunk.splitlines():
                        line = str(line).replace('\'', '').replace('b', '')
                        line = line.split(':')
                        if not SlovakiaApplicant.objects.filter(username=line[0], passport=line[1]).first():
                            form = SlovakiaApplicantForm(data={'username': line[0], 'passport': line[1], 'applicant_type': 'fake', 'priority': 0})
                            if form.is_valid():
                                SlovakiaApplicant.objects.create(**form.cleaned_data)
                                counter += 1
                messages.success(request, f'{counter} fake user added to the database.')
        else:
            username = request.POST.get('username', None)
            passport = request.POST.get('passport', None)
            if not username or not passport:
                messages.error(request, 'Username or passport cannot be empty.', extra_tags='danger')
            else:
                if SlovakiaApplicant.objects.filter(username=username, passport=passport).first():
                    messages.info(request, 'This user already exists in the database.')
                else:
                    form = SlovakiaApplicantForm(request.POST)
                    if form.is_valid():
                        SlovakiaApplicant.objects.create(**form.cleaned_data)
                        messages.success(request, 'A new user added to the database.')
                    else:
                        messages.error(request, 'You have put some invalid data in the form.', extra_tags='danger')
    return redirect('applicant-slovakia')


def slovakia_edit_applicant(request, id):
    if request.method == 'POST':
        applicant = get_object_or_404(SlovakiaApplicant, pk=id)
        username = request.POST.get('username', None)
        passport = request.POST.get('passport', None)
        if not username or not passport:
            messages.error(request, 'Username or passport cannot be empty.', extra_tags='danger')
        else:
            form = SlovakiaApplicantForm(request.POST)
            if form.is_valid():
                applicant.username = form.cleaned_data.get('username')
                applicant.passport = form.cleaned_data.get('passport')
                applicant.priority = form.cleaned_data.get('priority')
                applicant.save()
                messages.success(request, 'User information has been updated.')
            else:
                messages.error(request, 'You have put some invalid data in the form.', extra_tags='danger')
    return redirect('applicant-slovakia')


def slovakia_delete_applicant(request, id):
    applicant = get_object_or_404(SlovakiaApplicant, pk=id)
    applicant.delete()
    messages.success(request, 'An applicant has been deleted.')
    return redirect('applicant-slovakia')


def slovakia_add_process(request):
    if request.method == 'POST':
        center_code = int(request.POST.get('center', None))
        month = int(request.POST.get('month', None))
        process_type = int(request.POST.get('process_type', None))
        number = int(request.POST.get('number', 1))
        center = Center.objects.get(code=center_code)
        if not center:
            messages.error(request, 'Invalid center selected.', extra_tags='danger')
        elif number <= 0:
            messages.info(request, 'At least 1 process has to be run.')
        else:
            country = Country.objects.filter(name='Slovakia').first()
            date_open_instance = DateOpen.objects.filter(
                country=country, center=center, month=month
            ).first()
            if not date_open_instance:
                DateOpen.objects.create(
                    country=country, center=center, month=month
                )
            for _ in range(number):
                SlovakiaProcess.objects.create(center=center, month=month, process_type=process_type)
            messages.success(request, f'Successfully created {number} new process.')
    return redirect('applicant-slovakia')


def slovakia_delete_process(request, process_id):
    process = get_object_or_404(SlovakiaProcess, pk=process_id)
    country = Country.objects.filter(name='Slovakia').first()
    center = process.center
    month = process.month
    process.delete()
    messages.success(request, 'Successfully deleted the process.')
    if not SlovakiaProcess.objects.filter(center=center, month=month).first():
        date_open_instance = DateOpen.objects.filter(
            country=country, center=center, month=month
        ).first()
        date_open_instance.delete()
    return redirect('applicant-slovakia')


# --------------------------- BRTA -------------------------------------
def brta(request):
    context = {
        'fake_applicants': BRTAApplicant.objects.filter(applicant_type='fake'),
        'original_applicants': BRTAApplicant.objects.filter(applicant_type='original')
    }
    return render(request, 'applicant/brta/home.html', context)


def brta_add_applicant(request):
    if request.method == 'POST':
        applicant_type = request.POST.get('applicant_type')
        if applicant_type == 'fake':
            if request.FILES:
                file = request.FILES['file']
                counter = 0
                for chunk in file.chunks():
                    for line in chunk.splitlines():
                        line = str(line).replace('\'', '').replace('b', '')
                        line = line.split(':')
                        if not BRTAApplicant.objects.filter(username=line[0], password=line[1]).first():
                            form = BRTAApplicantForm(data={'username': line[0], 'password': line[1], 'applicant_type': 'fake', 'priority': 0})
                            if form.is_valid():
                                BRTAApplicant.objects.create(**form.cleaned_data)
                                counter += 1
                messages.success(request, f'{counter} fake user added to the database.')
        else:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            if not username or not password:
                messages.error(request, 'Username or password cannot be empty.', extra_tags='danger')
            else:
                if BRTAApplicant.objects.filter(username=username, password=password).first():
                    messages.info(request, 'This user already exists in the database.')
                else:
                    form = BRTAApplicantForm(request.POST)
                    if form.is_valid():
                        BRTAApplicant.objects.create(**form.cleaned_data)
                        messages.success(request, 'A new user added to the database.')
                    else:
                        messages.error(request, 'You have put some invalid data in the form.', extra_tags='danger')
    return redirect('applicant-brta')


def brta_edit_applicant(request, id):
    if request.method == 'POST':
        applicant = get_object_or_404(BRTAApplicant, pk=id)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if not username or not password:
            messages.error(request, 'Username or password cannot be empty.', extra_tags='danger')
        else:
            form = BRTAApplicantForm(request.POST)
            if form.is_valid():
                applicant.username = form.cleaned_data.get('username')
                applicant.password = form.cleaned_data.get('password')
                applicant.priority = form.cleaned_data.get('priority')
                applicant.save()
                messages.success(request, 'User information has been updated.')
            else:
                messages.error(request, 'You have put some invalid data in the form.', extra_tags='danger')
    return redirect('applicant-brta')


def brta_delete_applicant(request, id):
    applicant = get_object_or_404(BRTAApplicant, pk=id)
    applicant.delete()
    messages.success(request, 'An applicant has been deleted.')
    return redirect('applicant-brta')
