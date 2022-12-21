from django.shortcuts import render,redirect

from users.forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile 


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
    pro = Profile.objects.get(user=request.user)
    
    context = {'profile': pro}
    return render(request,'users/profile.html',context=context)


def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        pro = Profile()
        pro.contact_number = contact_number
        pro.image = image
        pro.user = request.user
        pro.save()
        return redirect('/users/profile')
    
    return render(request,'users/createprofile.html')
