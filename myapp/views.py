from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    d = {
        "name":"arun",
        "age":30,
    }
    
    li = ["allen","sreerag","alwin","justin","allu","hari"]
    
    context ={'li': li}
     
    return render(request,'index.html')

 