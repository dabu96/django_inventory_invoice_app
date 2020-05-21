from django import forms

from .models import Session


class BeginAccountCreationForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('production', 'site_id')
