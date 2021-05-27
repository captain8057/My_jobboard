from django.forms import ModelForm
from job.models import apply ,Job
from django import forms


class applyform(ModelForm):
    class Meta:
        model = apply
        fields='__all__'      




class JobForm(ModelForm):
    # Dead = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta:
        model = Job
        fields = [ 'title','job_type','descripyion','Vacancy','salary','experience','category','image','Country','Place']
        # exclude =('slug','onwer','like','published_at')


class JobFormDate(ModelForm):
    date =date = forms.DateTimeField(label="",
                    input_formats=['%d/%m/%Y %H:%M'],
                    widget=forms.DateTimeInput(attrs={
                            'class': 'form-control datetimepicker-input',
                            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        model = Job
        fields = [ 'date']


      



