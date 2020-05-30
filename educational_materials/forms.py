from django import forms
from .models import CreateHW


class CreateHWForm(forms.ModelForm):
    class Meta:
        model = CreateHW
        fields = ('published', 'title', 'about', 'image', 'file', 'source',)

