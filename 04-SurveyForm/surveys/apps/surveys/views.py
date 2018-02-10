from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'idx' not in request.session:
        request.session['idx'] = 0
    return render(request, "surveys/index.html")

def process(request):
    if request.method == "POST":
        request.session['idx'] += 1 
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return render(request,'surveys/result.html')
    else:
        return redirect("/")

def result(request):
    return redirect('/')

def reset(request):
    request.session['idx'] = 0
    request.session['name'] = ''
    request.session['location'] = ''
    request.session['language'] = ''
    request.session['comment'] = ''
    return redirect("/")