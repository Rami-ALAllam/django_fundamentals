from django.shortcuts import render, redirect

def survey(request):
    return render(request,"survey.html")

def result(request):
    name1 = request.POST['name']
    city1 = request.POST['city']
    lang1 = request.POST['lang']
    comment1 = request.POST['comment']
    context = {
        "name": name1,
        "city": city1,
        "lang": lang1,
        "comment": comment1
    }
    return render(request,"result.html",context)
