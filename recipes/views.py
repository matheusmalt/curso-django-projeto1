from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Página Home</h1>")

def contatcs(request):
    return HttpResponse("<h1>Página de Contatos</h1>")

def about(request):
    return HttpResponse("<h1>Página de Sobre</h1>")

