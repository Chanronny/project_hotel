from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'pages/index.html')
#    return HttpResponse("<h1>Index : Hello World !</h1>")

def about(request):
    return render(request,'pages/about.html')
#    return HttpResponse("<h1>About : Hello World !</h1>")