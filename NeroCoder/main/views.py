from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница DogDjango', "active": 1})

def new(request):
    return render(request, 'main/new.html', {'title': 'Новые открытия в области океанской флоры', "active": 2})

def plankton(request):
    return render(request, 'main/plankton.html', {'title': 'Польза планктона', "active": 3})

def crabs(request):
    return render(request, 'main/crabs.html', {'title': 'Океанские крабы', "active": 4})

def octopus(request):
    return render(request, 'main/octopus.html', {'title': 'Осьминоги', "active": 5})

def bivalves(request):
    return render(request, 'main/bivalves.html', {'title': 'Океанские двустворчатые моллюски', "active": 6})