from django.shortcuts import render
from django.http import HttpResponse
from roomtypes.models import Roomtype
# Create your views here.

def index(request):
    return render(request,'pages/index.html')
#    return HttpResponse("<h1>Index : Hello World !</h1>")

def about(request):
    roomtypes = Roomtype.objects.order_by('-room_type')
    context = {"roomtypes" : roomtypes}
    return render(request, 'pages/about.html', context)
#    return HttpResponse("<h1>About : Hello World !</h1>")