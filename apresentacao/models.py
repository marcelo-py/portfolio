from django.db import models
from django import forms
from django.utils import timezone

class Usuario(models.Model):
    usuario = models.CharField(default='Anônimo', max_length=25)
    mensagem = models.CharField(max_length=120)
    data_da_mensagem = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.usuario


class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('data_da_mensagem',)

