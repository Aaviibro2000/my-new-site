from django.shortcuts import render

from users.forms import NewUserForm





def register(request):
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(f'form valid : {form.is_valid()}')
        
        if form.is_valid:
            form.save()
        
    form = NewUserForm(request.POST)    
    context = {
        'form' : form,
    }
    
    return render(request,'users/register.html ',context)
