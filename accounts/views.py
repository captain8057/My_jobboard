from django.shortcuts import render,redirect,reverse
from .forms import SignupForm ,UserForm,ProfileForm
from django.contrib.auth import authenticate ,login
from accounts.models import profile , Normal_Users , Organisations,Expereions
from .decorators import *

# Create your views here.


@notLoggedUsers
def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           user = authenticate(username=username, password=password)
           login(request, user)
           return redirect(reverse('registration/login_register.html'))


    else:
        form = SignupForm()



    return render(request,'registration/signup.html',{'form':form})






def Profile(request):

    group= request.user.groups.all()[0].name
    if group=="Normal_Users":
        Profile = Normal_Users.objects.get(user=request.user)
        expereions = Expereions.objects.filter(user=request.user)
    else:
        org = Organisations.objects.get(user=request.user)
    if group=="Normal_Users":
        return render(request,'accounts/profile.html',{'Profile':Profile,'group':group,'expereions':expereions})
    else:
        return render(request,'accounts/Org_profile.html',{'org':org,'group':group})





def profile_edit(request):
    profilee = profile.objects.get(user=request.user)
    if request.method=="POST":
         userform = UserForm(request.POST,instance=request.user)
         profileform = ProfileForm(request.POST,request.FILES,instance=profilee )
         if userform.is_valid() and profileform.is_valid():
             userform.save()
             myprofile= profileform.save(commit=False)
             myprofile.user= request.user
             myprofile.save()
             return redirect(reverse('accounts:profile'))


    else:
         userform=UserForm(instance=request.user)
         profileform = ProfileForm(instance=profilee)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})

@notLoggedUsers
def login(request):
        return redirect(reverse('registration/login.html'))


def logoutUser(request):
        return redirect('templates/registration/logout.html')





def normal_users(request):
    Profile = Normal_Users.objects.get(user=request.user)
    group= request.user.groups.all()[0].name
    return render(request,'accounts/profile.html',{'Profile':Profile,'group':group})

