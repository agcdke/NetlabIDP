from django.shortcuts import render
from .models import OpcuaServerInfo


# Create your views here.
def home (request):
    context={
        "servers": OpcuaServerInfo.objects.all()
    }
    return render(request, 'idpdatacollection/home.html', context)

def about (request):
    return render(request, 'idpdatacollection/about.html', {'title': 'About'})