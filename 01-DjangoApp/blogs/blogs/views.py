from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    response = "(1) placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "(2) placeholder to display a new form to create a NEW blog"
    return HttpResponse(response)

def create(request):
    response = "(3) ## create ##"
    return redirect('/')

def show(request):
    response = "(4) placeholder to SHOW blog {{number}}"
    return HttpResponse(response)

def edit(request):
    response = "(5) placeholder to EDIT blog {{number}}"
    return HttpResponse(response)

def destroy(request):
    response = "(6) ## destroy ##"
    return redirect('/')