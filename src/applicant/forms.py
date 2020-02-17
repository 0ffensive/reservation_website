from django import forms


class SlovakiaApplicantForm(forms.Form):
    username = forms.CharField(required=True, max_length=100)
    passport = forms.CharField(required=True, max_length=100)
    applicant_type = forms.CharField(required=True)
    priority = forms.IntegerField()


class BRTAApplicantForm(forms.Form):
    username = forms.CharField(required=True, max_length=100)
    password = forms.CharField(required=True, max_length=100)
    applicant_type = forms.CharField(required=True)
    priority = forms.IntegerField()
