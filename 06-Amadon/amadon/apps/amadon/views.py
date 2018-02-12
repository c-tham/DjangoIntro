from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'history' not in request.session:
        request.session['cart1'] = 0
        request.session['cart2'] = 0
        request.session['history'] = 0
    context = {
        "name" : "Amadon"
    }
    return render(request, "amadon/index.html", context)

def buy(request):
    print "** buy post"
    prod_ID = {
        '101': 19.99,
        '102': 29.99,
        '103': 4.99,
        '104': 49.99
    }
    print request.POST['product_id'], request.POST['price'], request.POST['qty']
    request.session['qty'] = int(request.POST['qty'])
    request.session['cart1'] = float(prod_ID[request.POST['product_id']]) * request.session['qty']
    request.session['cart2'] = float(request.POST['price']) * request.session['qty']
    request.session['history'] += request.session['cart1']
    print request.session['qty'], request.session['cart1'], request.session['cart2'], request.session['history'] 
    return redirect("/checkout")

def checkout(request):
    context = {
        "name" : "Amadon",
        "total1" : request.session['cart1'],
        "total2" : request.session['cart2'],
        "quantity" : request.session['qty'],
        "history" : request.session['history']
    }
    return render(request, "amadon/checkout.html", context)

def reset(request):
    request.session['cart1'] = 0
    request.session['cart2'] = 0
    request.session['history'] = 0
    context = {
        "name" : "Amadon"
    }
    return redirect('/')