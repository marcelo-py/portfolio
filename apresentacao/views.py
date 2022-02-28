from django.shortcuts import render, redirect
from .models import Usuario, FormUsuario


def index(request):
    dados = Usuario.objects.all()
    form = FormUsuario()
    if request.method != 'POST':
        return render(request, 'paginas/index.html',{
            'mensagens': dados,
            'usuario': form
        })
    
    form = FormUsuario(request.POST)
    if form.is_valid:
        form.save()
    return redirect('index')