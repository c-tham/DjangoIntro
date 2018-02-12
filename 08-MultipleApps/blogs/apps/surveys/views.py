from django.shortcuts import render, HttpResponse, redirect

def html(request):
    context = {
        "name" : "surveys"
    }
    return render(request, "surveys/index.html", context)

def index(request):
    response = "SURVEYS (1) placeholder to display all the surveys created"
    print response
    return HttpResponse(response)

def new(request):
    response = "SURVEYS (2) placeholder for users to add a new survey"
    print response
    return HttpResponse(response)
