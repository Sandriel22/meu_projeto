from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'global/home.html')

def sobre(request):
    return render(request, 'global/sobre.html')

def contato(request):
    return render(request, 'global/contato.html')