from django import forms
from .models import DashModel

class DashForm(forms.ModelForm):
    class Meta:
        model = DashModel
        fields = '__all__'