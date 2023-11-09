from django.shortcuts import render
from time import gmtime, strftime, localtime

def time1(request):
    context = {
        "date": strftime("%b %d, %Y",gmtime()),
        "time": strftime("%I:%M %p",localtime())
    }
    return render(request, 'time.html', context)

def time2(request):
    context = {
        "date": strftime("%d-%m-%Y",gmtime()),
        "time": strftime("%H:%M:%S",localtime())
    }
    return render(request,'time.html', context)

def time3(request):
    context = {
        "date": strftime("%a, %d %b %Y %H:%M:%S", gmtime()),
        "time": strftime("%I:%M %p",localtime())
    }
    return render(request,'time.html', context)