from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'meu_app/home.html')

def sobre(request):
    return render(request, 'meu_app/sobre.html')

def contato(request):
    return render(request, 'meu_app/contato.html')