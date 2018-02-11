from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    if "activities" not in request.session:
        request.session['activities'] = []
    context = {
        "name" : "ninja_gold"
    }
    return render(request, "ninja_gold/index.html", context)

def process_money(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    if "activities" not in request.session:
        request.session['activities'] = []
    print "process_money"
    now = datetime.now()
    if request.POST['building'] == 'farm':
        randNum = random.randrange(10,21)
        request.session['gold'] += randNum
        request.session['activities'].append('Earned '+str(randNum)+' from the farm! ('+str(now)+')')
    elif request.POST['building'] == 'cave':
        randNum = random.randrange(5,11)
        request.session['gold'] += randNum
        request.session['activities'].append('Earned '+str(randNum)+' from the cave! ('+str(now)+')')
    elif request.POST['building'] == 'house':
        randNum= random.randrange(2,6)
        request.session['gold'] += randNum
        request.session['activities'].append('Earned '+str(randNum)+' from the house! ('+str(now)+')')
    elif request.POST['building'] == 'casino':
        randNum = random.randrange(-50,51)
        request.session['gold'] += randNum
        if randNum >= 0:
            request.session['activities'].append('Earned '+str(randNum)+' from the casino! ('+str(now)+')')
        else:
            request.session['activities'].append('Entered a casino and lost '+str(randNum)+' golds... Ouch... ('+str(now)+')')
    print randNum, request.session['gold']
    return redirect('/')

def reset(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    if "activities" not in request.session:
        request.session['activities'] = []
    print "reset"
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')