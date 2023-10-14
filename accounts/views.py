from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('This is the home page.')

def products(request):
    return HttpResponse('This is the products page')

def about(request):
    return HttpResponse('This is the about page.')
