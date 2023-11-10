from django.shortcuts import render, redirect

def count1(request):
    if 'count' in request.session:
        print('key exists!')
        request.session['count'] += 1
    else:
        print("key 'count' does NOT exist")
        request.session['count'] = 1
    return render(request, "count.html")

def count2(request):
    if 'count' in request.session:
        print('key exists!')
        request.session['count'] += 1
    else:
        print("key 'count' does NOT exist")
        request.session['count'] = 1
    return redirect("/")

def count3(request):
    num = int(request.POST['num'])
    if 'count' in request.session:
        print('key exists!')
        request.session['count'] += (num-1)
    else:
        print("key 'count' does NOT exist")
        request.session['count'] = 1
    return redirect("/")


def destroy_session(request):
    del request.session['count']
    return redirect("/")

