from django import forms
from .models import Matrice

class MatriceForm(forms.ModelForm):
    class Meta:
        model = Matrice
        fields = ['login', 'Nom', 'Prenom', 'Role', 'Situation']
        labels = {
            'login': 'Login',
            'Nom': 'Nom',
            'Prenom': 'Prénom',
            'Role': 'Rôle',
            'Situation': 'Situation'
        }
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'Nom': forms.TextInput(attrs={'class': 'form-control'}),
            'Prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'Role': forms.TextInput(attrs={'class': 'form-control'}),
            'Situation': forms.Select(attrs={'class': 'form-control'})
        }
