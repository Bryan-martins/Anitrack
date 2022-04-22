from django import forms
from .models import ListaUser


class PostForm(forms.ModelForm):
    class Meta:
        model = ListaUser
        fields = ('data_inicio', 'data_fim', 'progress', 'status')
        