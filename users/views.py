from django.shortcuts import render

from users.forms import NewUserForm





def register(request):
    
    form = NewUserForm(request.POST)
    context = {
        'form' : form,
    }
    
    return render(request,'users/register.hmtl',context)
