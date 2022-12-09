from django.shortcuts import render,redirect

from users.forms import NewUserForm



def register(request):
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(f'form valid : {form.is_valid()}')
        if form.is_valid:
            form.save()
            
            
        return redirect('/myapp/products')
    form = NewUserForm(request.POST)    
    context = {
        'form' : form,
    }
    
    return render(request,'users/register.html ',context)
