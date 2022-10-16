from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    d = {
        "name":"arun",
        "age":30,
    }
    
    return render(request,'index.html')

 