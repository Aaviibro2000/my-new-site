from django.shortcuts import render

from users.forms import NewUserForm





def register(request):
    
    form = NewUserForm(request.POST)
    context = {
        'f' : form,
    }
    
    return render(request,'users/register.html ',context)
