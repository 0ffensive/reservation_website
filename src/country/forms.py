from django import forms


class CountryForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    url = forms.URLField(required=True, max_length=400)


class CenterForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    code = forms.IntegerField(required=True)
    country = forms.IntegerField(required=True)
