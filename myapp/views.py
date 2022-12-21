from multiprocessing import context

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def products_details(request,id):
    p = product.objects.get(id=id)
    context={'p':p}
    return render(request,'myapp/products_details.html',context=context)

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        details = request.POST.get('details')
        image = request.FILES['upload']
        p=product(name=name,price=price,description=desc,image=image)
        p.save()
        
        return redirect('/myapp/products')
        
    return render(request,'myapp/add_product.html')

def update_product(request,id):
    p = product.objects.get(id=id)
    context = {'p':p}
    
    
    if request.method == 'POST':
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.description = request.POST.get('desc')
        p.details = request.POST.get('details')
        try:
            p.image = request.FILES['upload']
        except:
            pass
        p.save()
        
        return redirect('/myapp/products')
        
    return render(request,'myapp/update_product.html',context=context)

def delete_product(request,id):
    p = product.objects.get(id=id)
    context = {'p':p}
    
    if request.method == 'POST':
        p.delete()
        
        
        
        return redirect('/myapp/products')
    
    
    return render(request,'myapp/delete_products.html',context=context)
    
    
    
    
    
    
    
    
    
    