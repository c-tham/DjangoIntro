from django.shortcuts import render, HttpResponse, redirect

from time import gmtime, strftime

def index(request):
    context = {
        # "date_time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        "date": strftime("%B %d, %Y", gmtime()),
        "time": strftime("%H:%M %p %z", gmtime())
    }
    return render(request,'time_display/index.html', context)

# def index(request):
#     response = "Hello, Welcome to time_display (Django App)!"
#     return HttpResponse(response)