from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def customers(request):
    return render(request, 'accounts/customers.html')

def products(request):
    return render(request, 'accounts/products.html')

def orders(request):
    return render(request, 'accounts/orders.html')
