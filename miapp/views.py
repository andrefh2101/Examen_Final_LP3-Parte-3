from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date

def saludo(request):
    return render(request, 'saludo.html')

def persona(request):
    return render(request, 'persona.html')

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import Fernandez_Persona
from .forms import PersonaForm

def personas(request):
    personas = Fernandez_Persona.objects.all()
    return render(request, 'persona.html', {'personas': personas})  # Nombre del contexto corregido

def agregar_persona(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        sexo = request.POST['sexo']

        persona = Fernandez_Persona(
            nombre=nombre,
            apellidos=apellidos,
            sexo=sexo,
        )
        persona.save()
        messages.success(request, f'Se agregó correctamente la persona {persona.nombre} {persona.apellidos}')
        return redirect('persona')  # Redirige a la vista de personas

    return render(request, 'agregar_persona.html')

def eliminar_persona(request, id):
    persona = get_object_or_404(Fernandez_Persona, id=id)
    persona.delete()
    messages.success(request, f'Se eliminó correctamente la persona {persona.nombre} {persona.apellidos}')
    return redirect('persona')

def editar_persona(request, id):
    persona = get_object_or_404(Fernandez_Persona, id=id)
    
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona actualizada correctamente.')
            return redirect('persona')
    else:
        form = PersonaForm(instance=persona)
    
    return render(request, 'editar_persona.html', {'form': form})
