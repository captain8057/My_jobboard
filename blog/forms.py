from django.forms import ModelForm
from .models import Post 
from django import forms
from crispy_forms.helper import FormHelper


class PostForm(ModelForm):
     class Meta:
        model = Post
        fields = ['title','content','image','Hyper_Text','tags']

        # widget = {
        #     'title': forms.TextInput(attrs={'class':'single-input'}),
        #     'content': forms.Textarea(attrs={'class':'single-textarea'}),
        #     'image': forms.FileInput(),
        #     'Hyper_Text': forms.TextInput(attrs={'class':'form-control form-control-sm','id':"formFileSm" ,'type':"file"}),
        #     'tags': forms.TextInput(attrs={'class':'form-select','style':'overflow-y:auto; max-height:80vh'}),
        # }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper(self)