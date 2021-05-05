from django.shortcuts import render,redirect,reverse
from .forms import SignupForm ,UserForm,ProfileForm,Org_ProfileForm,Org_UserForm
from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import Group
from django.contrib import messages
from accounts.models import *
from .decorators import *
import requests 
from django.conf import settings 
from job.models import Job

# Create your views here.


@notLoggedUsers
def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                     'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                     'response' : recaptcha_response
                   }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
            result = r.json()
            if result['success']:
                user= form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect('/accounts/profile')
            else:
                messages.error(request ,  ' invalid Recaptcha please try again!')  
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})






def Profile(request):

    group=  request.user.groups.all()[0].name
    if group=="Normal_Users":
        Profile = Normal_Users.objects.get(user=request.user)
        expereions = Expereions.objects.filter(user=request.user)
        courses = Courses.objects.filter(user=request.user)
        academic = Academic_Background.objects.filter(user=request.user)
        like = Job.objects.filter(like=request.user)
    else:
        org = Organisations.objects.get(user=request.user)
    if group=="Normal_Users":
        return render(request,'accounts/profile.html',{'Profile':Profile,'group':group,'expereions':expereions,'courses':courses,'academic':academic ,'like':like})
    else:
        return render(request,'accounts/Org_profile.html',{'org':org,'group':group})




@allowedUsers(allowedGroups=['Normal_Users'])
def profile_edit(request):
    profilee = Normal_Users.objects.get(user=request.user)
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

# @notLoggedUsers
# def login(request):
#         return redirect(reverse('registration/login.html'))


def logoutUser(request):
        return redirect('templates/registration/logout.html')





def normal_users(request):
    Profile = Normal_Users.objects.get(user=request.user)
    group= request.user.groups.all()[0].name
    return render(request,'accounts/profile.html',{'Profile':Profile,'group':group})

@allowedUsers(allowedGroups=['Admin','Organisations'])
def org_profile_edit(request):
    profilee = Organisations.objects.get(user=request.user)
    if request.method=="POST":
         userform = Org_UserForm(request.POST,instance=request.user)
         profileform = Org_ProfileForm(request.POST,request.FILES,instance=profilee )
         if userform.is_valid() and profileform.is_valid():
             userform.save()
             myprofile= profileform.save(commit=False)
             myprofile.user= request.user
             myprofile.save()
             return redirect(reverse('accounts:profile'))


    else:
         userform=Org_UserForm(instance=request.user)
         profileform = Org_ProfileForm(instance=profilee)

    return render(request,'accounts/org_profile_edit.html',{'userform':userform , 'profileform':profileform})