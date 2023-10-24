from django import forms
from .models import Geeks
class GeeksForm(forms.ModelForm):
    class Meta:
        model=Geeks
        fields=["title","description"]

