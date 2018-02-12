from django.shortcuts import render, HttpResponse, redirect

# def index0(request):
#     context = {
#         "name" : "blogs"
#     }
#     return render(request, "blogs/index.html", context)

def index(request):
    response = "BLOGS (1) placeholder to later display all the list of blogs"
    print response
    return HttpResponse(response)

def new(request):
    response = "BLOGS (2) placeholder to display a new form to create a NEW blog"
    print response
    return HttpResponse(response)

def create(request):
    response = "BLOGS (3) ## create blog ##"
    print response
    return redirect('/blogs')

def show(request, num):
    response = "BLOGS (4) placeholder to SHOW blog at {}.".format(num)
    print response
    return HttpResponse(response)

def edit(request, num):
    response = "BLOGS (5) placeholder to EDIT blog at {}.".format(num)
    print response
    return HttpResponse(response)

def destroy(request, num):
    response = "BLOGS (6) ## destroy blog ##"
    print response
    return redirect('/blogs')

def main(request):
    response = "BLOGS (7) ## route to blog index ##"
    print response
    return redirect('/blogs')