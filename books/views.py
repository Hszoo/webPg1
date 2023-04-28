from django.shortcuts import render

# Create your views here.
def bookHome(request) :
    return render(request, "templates/bookHome.html")

def bookSecond(request) :
    return render(request, "templates/bookSecond.html")