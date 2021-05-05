from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import *




class SignupForm(UserCreationForm):
   class Meta:
        model = User
        fields = ['username','email','password1','password2']




class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        exclude = ['user']




class ProfileForm(ModelForm):
    class Meta:
       model = Normal_Users
       fields = "__all__"
       exclude = ['user']
       
        

class Org_ProfileForm(ModelForm):
    class Meta:
       model = Organisations
       fields = "__all__"
       exclude = ['user']


class Org_UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ["username","email"]
        exclude = ['user',"first_name","last_name"]