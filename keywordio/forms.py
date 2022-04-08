from django import forms
from django.forms import fields
from keywordio.models import book
from keywordio.models import student

class bookenter(forms.ModelForm):
    class Meta:
        model=book
        fields = '__all__'
class studententer(forms.ModelForm):
    class Meta:
        model=student
        fields = '__all__'
