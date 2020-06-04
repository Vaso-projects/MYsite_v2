from django import forms
from .models import Homework


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('published', 'title', 'about', 'image', 'content',  'file', 'source',)


class HomeworkForm2(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('title', 'about', 'content', 'file', 'source',)
