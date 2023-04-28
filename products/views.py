from django.shortcuts import render

# Create your views here.

def productHome(request) :
    return render(request, "templates/productsHome.html")

def productSecond(request) :
    return render(request, "templates/productsSecond.html")