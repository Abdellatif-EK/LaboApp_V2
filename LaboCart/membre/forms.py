from django import forms
from .models import Analyste

class AnalysteForm(forms.ModelForm):
    class Meta:
        model = Analyste
        fields = ['first_name', 'last_name', 'email', 'password', 'phone']
        labels = {
            'first_name': 'Nom',
            'last_name': 'Prénom',
            'email': 'Email',
            'password': 'Mot de passe',
            'phone': 'Téléphone'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
        }