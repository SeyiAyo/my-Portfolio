# forms.py
from django import forms
from .models import contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField()
    
    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'message']
