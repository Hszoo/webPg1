from django.shortcuts import render

# Create your views here.

def shopHome(request) : 
    return render(request, "shopHome.html")

def shopSecond(request) : 
    return render(request, "shopSecond.html")