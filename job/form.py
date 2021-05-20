from django.forms import ModelForm
from job.models import apply ,Job



class applyform(ModelForm):
    class Meta:
        model = apply
        fields='__all__'      




class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__' 
        exclude =('slug','onwer','like','published_at')


      



