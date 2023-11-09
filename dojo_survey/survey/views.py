from django.shortcuts import render, redirect

def survey(request):
    return render(request,"survey.html")

def result(request):
    name1 = request.POST['name']
    gender1 = request.POST['gender'] 
    city1 = request.POST['city']
    lang1 = request.POST['lang']
    comment1 = request.POST['comment']
    offer1 = request.POST['offers']
    context = {
        "name": name1,
        "gender": gender1,
        "city": city1,
        "lang": lang1,
        "comment": comment1,
        "offers" : offer1
    }
    return render(request,"result.html",context)
