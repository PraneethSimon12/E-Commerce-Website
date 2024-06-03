from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.messages import messages
from django.contrib.auth.models import User

# Create your views here.

def login_page(request):
    return render(request,'accounts/login.html')

def register_page(request):

    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request,'Email is already is taken')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name = first_name , last_name = last_name , 
                                       email = email , username = email )
        user_obj.set_password(password)
        

    return render(request,'accounts/register.html')