from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def galeria(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())
def aboutUs(request):
    template = loader.get_template('about-us.html')
    return HttpResponse(template.render())
def loginPage(request):
    template = loader.get_template('login-page.html')
    return HttpResponse(template.render())


