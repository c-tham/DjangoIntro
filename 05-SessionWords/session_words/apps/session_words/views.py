from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    if 'word_list' not in request.session:
        list_word = []
        request.session['word_list'] = list_word 
    context = {
        "name" : "Session_Words"
    }
    return render(request, "session_words/index.html", context)

def add_word(request):
    if request.method == "POST":
        if len(request.POST['word']) > 0:
            list_new = {
                'word': request.POST['word'],
                'color': request.POST['color'],
                'size': request.POST['size'],
                'datetime': str(datetime.now())
            }
            print list_new
            list_word = request.session['word_list']
            list_word.append(list_new)
            request.session['word_list'] = list_word
            print request.session['word_list']
    return redirect("/")

def clear(request):
    list_word = []
    request.session['word_list'] = list_word
    return redirect("/")