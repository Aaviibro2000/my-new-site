from django.shortcuts import render,redirect

from users.forms import NewUserForm
from django.contrib.auth.decorators import login_required


def register(request):
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(f'form valid : {form.is_valid()}')
        if form.is_valid():
            form.save()
            
            
        return redirect('/myapp/products')
    form = NewUserForm(request.POST)    
    context = {
        'form' : form,
    }
    
    return render(request,'users/register.html ',context)


def profile(request):
    return render(request,'users/profile.html')


def create_profile(request):
    if request.method == 'POST':
        pass
    
    return render(request,'users/createprofile')
