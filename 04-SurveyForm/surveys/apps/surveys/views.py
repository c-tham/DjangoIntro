from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
        "name" : "surveys"
    }
    return render(request, "surveys/index.html", context)
