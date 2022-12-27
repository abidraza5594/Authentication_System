from django.shortcuts import render,redirect
from users.forms import UserRegisterForm,Edit_Profile_Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_Profile
# Create your views here.
def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'successfull Register...!')
            return redirect('login')

    else:
        form=UserRegisterForm()
    context={
        'form':form,
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')

def editprofile(request,id):
    if request.method=="POST":
        user=User_Profile.objects.get(id=id)
        form=Edit_Profile_Form(data=request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=Edit_Profile_Form()

    return render(request,'users/editprofile.html',{'form':form})