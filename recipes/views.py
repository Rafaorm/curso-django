from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', status=201, context={
                  'name': 'RORM',})

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')
