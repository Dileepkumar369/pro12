from django.http import HttpResponse
from django.shortcuts import render
def views1 (request):
    return HttpResponse("<h1>urls in myapp</h1>")
def views2(request,email):
    return render(request,"views2.html",context={'email':email,'name':"dileh"})
def views3(request,name):
    return HttpResponse(f'<h1>Hello Mr./Ms. {name}</h1>')