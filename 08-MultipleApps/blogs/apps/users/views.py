from django.shortcuts import render, HttpResponse, redirect

def html(request):
    context = {
        "name" : "users"
    }
    return render(request, "users/index.html", context)

def index(request):
    response = "USERS (1) placeholder to later display all the list of users"
    print response
    return HttpResponse(response)

def new(request):
    response = "USERS (2) placeholder to display a new form to create"
    print response
    return HttpResponse(response)

def register(request):
    response = "USERS (3) placeholder for users to create a new user record"
    print response
    return HttpResponse(response)

def login(request):
    response = "USERS (4) placeholder for users to login"
    print response
    return HttpResponse(response)