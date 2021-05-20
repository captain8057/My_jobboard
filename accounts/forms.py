from django.forms import ModelForm , Textarea
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.utils.translation import gettext_lazy as _
from django import forms


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
       labels = {
            'First_Name': _('Writer'),
        }
       widgets = {
            'First_Name':Textarea(attrs={'cols': 80, 'rows': 20}),
            'Birth_Date':forms.DateInput(attrs={'cols': 80, 'rows': 20}),
            
        }
       help_texts = {
            'First_Name': _('Some useful help text.'),
        }
       error_messages = {
            'Birth_Date': {
                'max_length': _("This writer's name is too long."),
            },
        }
       
        

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