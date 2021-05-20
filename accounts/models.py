from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from PIL import Image

# Create your models here.




class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    phone_number =  models.CharField(max_length=15)
    image = models.ImageField(upload_to="profile/")
    city_name = models.ForeignKey("city",on_delete=models.CASCADE , null=True)

    def __str__(self):
        return str(self.user)
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


class city(models.Model):
    name = models.CharField( max_length=20)

    def __str__(self):
        return str(self.name)



Marital_status=(
    ("single","single"),
    ("Married","Married"),
    ("divorced","divorced"),
    ("widowed","widowed"),


)

gender=(
    ("Male","Male"),
    ("Female","Female"),


)

class Normal_Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name =  models.CharField(null=True, max_length=50)
    Midle_Name =  models.CharField(null=True, max_length=50)
    Last_Name =  models.CharField(null=True, max_length=50)
    Photo = models.ImageField(upload_to="profile/" ,null=True , default="profile/person.jpg")
    city_name = models.ForeignKey("city",on_delete=models.CASCADE , null=True)
    Birth_Date = models.DateField(null=True)
    Soical_State = models.CharField(max_length=20 , choices=Marital_status ,null=True)
    Phone_Number =  models.CharField(max_length=15,null=True)
    Country = CountryField(null=True)
    Gender = models.CharField(max_length=20 , choices= gender,null=True)

    def __str__(self):
        return str(self.user)






class Organisations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    About= models.TextField(max_length=1000,null=True)
    Name =  models.CharField(null=True, max_length=50)
    Photo = models.ImageField(upload_to="profile/")
    city_name = models.ForeignKey("city",on_delete=models.CASCADE , null=True)
    Creat_Date = models.DateField()
    Phone_Number =  models.CharField(max_length=15)
    Headquarters = CountryField()

    def __str__(self):
        return str(self.Name)

    def save(self):
        super().save()

        img = Image.open(self.Photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Photo.path)








class Expereions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    Job_Title = models.CharField(null=True, max_length=50)
    Organisation = models.CharField(null=True, max_length=50)
    Duration = models.DurationField(null=True, max_length=50)
    From_Date = models.DateField()
    To_Date = models.DateField()
    Country = CountryField()
    city_name = models.ForeignKey("city",on_delete=models.CASCADE , null=True)
    Location = models.CharField(null=True, max_length=50)
    Responsibilities = models.TextField(help_text = 'Input your Exp',null= True)


    def __str__(self):
        return str(self.Job_Title)



class Courses(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    Cours_Name = models.CharField(null=True, max_length=50)
    Company = models.CharField(null=True, max_length=50)
    Type = models.CharField(null=True, max_length=50)
    Country = CountryField()
    city_name = models.ForeignKey("city",on_delete=models.CASCADE , null=True)
    race_start = models.DateTimeField()
    race_finish = models.DateTimeField(blank=True, null=True)
    @property
    def duration(self):
        if not (self.race_start and self.race_finish): return None
        a,b=self.race_start, self.race_finish
        return '%s:%s' % ((b-a).days*24 + (b-a).seconds//3600, (b-a).seconds%3600//60)
    
    def __str__(self):
        return str(self.Cours_Name)





Certificate=(
            (" High School"," High School"),
            ("University student","University student"),
            ("diploma","diploma"),
            ("Intermediate Institute ","Intermediate Institute "),
            ("Bachelor's ","Bachelor's "),
            ("Master's ","Master's "),
            ("Ph.D.","Ph.D."),
)

class Academic_Background(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    Certificate_Type= models.CharField( max_length=50, choices= Certificate)
    University_Name = models.CharField( max_length=50)
    specialization = models.CharField( max_length=50)
    Location = models.CharField( max_length=50)
    Duration = models.CharField( max_length=50)
    From_Date = models.DateField()
    To_Date = models.DateField()
    GPA = models.FloatField()
    
    def __str__(self):
        return str( "{}  -  {}" .format(self.Certificate_Type,self.specialization))
     