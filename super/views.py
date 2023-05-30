# from django.http import HttpResponse
# from datetime import datetime
from django.shortcuts import render,redirect
from .forms import  createUserForm
from django.contrib import messages
from .models import RegisterField
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



 
def home(request):
    data=RegisterField.objects.all()
    if (data!=''):                                                     
      return render(request,"home.html",{'data':data})        
    else:
      return render(request,"home.html")
                                                    
def register(request):
    if request.method == 'POST':
          username=request.POST["username"]
          email=request.POST["email"]
          password1=request.POST["password1"]
          password2=request.POST["password2"]
          if password1==password2:    
            user=User.objects.create_user(username=username, email=email, password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account has been created! You are now able to log in.')
            return redirect('login')
          else: 
            messages.warning(request,'Password mismatch! Please try again.') 
            return redirect('register')
    else:          
          form=createUserForm()
          return render(request,"register.html",{'form':form})
@login_required        
def profile(request):
      return render(request,"profile.html")
    
    
        
  
   

          
 


