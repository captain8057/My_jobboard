from django.db import models
from django_slugify_processor.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from PIL import Image
from django.utils import timezone
# Create your models here.


'''
    import from moodle for :
    -htmal widget
    -validation
    - db size 

'''

Job_Type=(
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
    ("OnLine","OnLine"),

)

def image_upload(inistans , filename):
    imagename , extension = filename.split(".")
    return "pic/%s/%s.%s"%(inistans.id,inistans.id,extension)


class Job(models.Model):  #tabdle

    onwer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='onwer_job')
    title = models.CharField(max_length=100) #column
    job_type = models.CharField(max_length=20 , choices= Job_Type)
    descripyion = models.TextField()
    published_at = models.DateTimeField(default=timezone.now,null=True)
    last_Update = models.DateTimeField(auto_now=True,null=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True , null= True)
    like = models.ManyToManyField(User , blank=True)
    Country = CountryField(null=True)
    Place =  models.CharField(max_length=100 , null= True,blank=True)
    Dead_line= models.DateTimeField(null= True)




    def save(self,*args ,**kwargs):
        self.slug = slugify(self.title) 
        #logic
        super(Job,self).save(*args,**kwargs)
        


    #return name of job in admin panal
    def __str__(self):
        return self.title



class Category(models.Model):
    Name = models.CharField(max_length=25)


    def __str__(self):
        return self.Name


class apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,related_name='apply_job')
    Candidate= models.ForeignKey(User, on_delete=models.CASCADE,related_name='apply_job',null=True)
    