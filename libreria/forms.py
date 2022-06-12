from dataclasses import fields
from django import forms
from django import forms
from.models import libro
from.models import usuario
from.models import adquisicion

class LibroForm(forms.ModelForm):
    class Meta:
        model=libro
        fields='__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=usuario
        fields='__all__'

class AdquisicionForm(forms.ModelForm):
    class Meta:
        model=adquisicion
        fields='__all__'