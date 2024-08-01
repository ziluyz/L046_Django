from django.http import HttpResponse

def data(request):
    return HttpResponse("<h1>Data page</h1>")

def test(request):
    return HttpResponse("<h1>Test page</h1>")