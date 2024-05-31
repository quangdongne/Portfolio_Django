from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'contact__input',
    }))
    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'contact__input',
    }))
    project = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'contact__input',
    }))
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={
        'class': 'contact__input',
        'rows': 7,
    }))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'project', 'message',)
