
from django.shortcuts import render, redirect
import random
from time import gmtime, strftime, localtime

def golden(request):

    if 'gold' in request.session:
        print('key exists!')

    else:
        print("key 'gold' does NOT exist")
        request.session['gold']=0
        request.session['moves']=0
        request.session['activities'] = []

    return render(request,"ninja.html")

def handle(request):

    if request.POST['gold_add'] == 'farm':
        request.session['amount'] = random.randint(2,5)
    elif request.POST['gold_add'] == 'cave':
        request.session['amount'] = random.randint(5,10)
    elif request.POST['gold_add'] == 'house':
        request.session['amount'] = random.randint(10,20)
    elif request.POST['gold_add'] == 'quest':
        request.session['amount'] = random.randint(-50,50)

    request.session['gold'] += request.session['amount']
    request.session['name'] = request.POST['gold_add']
    request.session['moves']+=1

    request.session['activities'].append({
        "gold" : request.session['amount'],
        "field" : request.session['name']
        })
    request.session.save()

    return redirect("/result")

def result(request):
    context = {
        "date": strftime("%B %d, %Y",gmtime()),
        "time": strftime("%I:%M %p",localtime())
    }
    return render(request,"ninja.html",context)

def reset(request):
    request.session.flush()
    return redirect ("/")



