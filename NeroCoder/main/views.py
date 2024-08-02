from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница DogDjango', "active": 1})

def new(request):
    return render(request, 'main/new.html', {"active": 2})

def plankton(request):
    return render(request, 'main/plankton.html', {"active": 3})

def crabs(request):
    return render(request, 'main/crabs.html', {"active": 4})

def octopus(request):
    return render(request, 'main/octopus.html', {"active": 5})

def bivalves(request):
    return render(request, 'main/bivalves.html', {"active": 6})