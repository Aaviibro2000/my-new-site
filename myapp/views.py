from multiprocessing import context

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from myapp.models import product


def index(request):
    d = {
        "name":"arun",
        "age":30,
    }
    
    li = ["allen","sreerag","alwin","justin","allu","hari"]
    
    for i in range (0,10):
        print(i)
        
    context ={'li': li}
     
    return render(request,'myapp/index.html',context=context)

def products(request):
    p = product.objects.all()
    context={'products':p}
    return render(request,'myapp/products.html',context=context)
