from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "name" : "Amadon"
    }
    return render(request, "amadon/index.html", context)

def checkout(request):
    context = {
        "name" : "Amadon"
    }
    return render(request, "amadon/checkout.html", context)