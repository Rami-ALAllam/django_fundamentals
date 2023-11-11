from django.shortcuts import render, redirect
import random

def num(request):
    if 'num' in request.session:
        print('num exists!')
        print(f"*************________{request.session['num']}_______*********************")
    else:
        print("key 'num' does NOT exist")
        request.session['num'] =random.randint(1,100)
        print(f"*************________{request.session['num']}_______*********************")

    if 'counter' in request.session:
        print('counter exists!')
    else:
        print("key 'counter' does NOT exist")
        request.session['counter'] = 0



    return render(request, "game.html")

def handle(request):
    request.session['guess']= int(request.POST['num1'])
    request.session['counter'] +=1
    return redirect('/result')

def result(request):
    context={
            "limit": 5
    }
    return render(request, "result.html", context)

def end(request):
    request.session.flush()
    return redirect("/")