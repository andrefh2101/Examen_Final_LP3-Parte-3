from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date

def saludo(request):
    return render(request, 'saludo.html')

def persona(request):
    return render(request, 'persona.html')

def index(request):
    return render(request, 'index.html')
