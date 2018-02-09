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

def show(request, num):
    response = "(4) placeholder to SHOW blog at {}.".format(num)
    return HttpResponse(response)

def edit(request, num):
    response = "(5) placeholder to EDIT blog at {}.".format(num)
    return HttpResponse(response)

def destroy(request, num):
    response = "(6) ## destroy ##"
    return redirect('/')