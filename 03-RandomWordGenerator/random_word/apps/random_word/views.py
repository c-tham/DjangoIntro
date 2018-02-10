from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'num' not in request.session:
        request.session['num'] = 0
        request.session['rand_wd'] = ''
    return render(request, "random_word/index.html")

def rand(request):
    if request.method == "POST":
        request.session['num'] += 1 
        request.session['rand_wd'] = get_random_string(length=14)
        return redirect("/")
    else:
        return redirect("/")

def reset(request):
    request.session['num'] = 0
    request.session['rand_wd'] = ''
    return redirect("/")