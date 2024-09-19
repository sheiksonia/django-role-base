from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer'),
        
    ]
    usertype=models.CharField(choices=USER,max_length=100,null=True)
    def __str__(self)-> str:
        return f"{self.username}-{self.first_name}-{self.last_name}"
    
class ResumeModel(models.Model):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    user=models.OneToOneField(customUser,null=True,on_delete=models.CASCADE)
    Contact_Number=models.CharField(max_length=100,null=True)
    Designation=models.CharField(max_length=100,null=True)
    Profile_pic=models.ImageField(upload_to="Media/Profile_Pic",null=True)
    Carer_Summary=models.TextField(max_length=100,null=True)
    age=models.PositiveIntegerField(max_length=100,null=True)
    gender=models.CharField(choices=GENDER, max_length=100,null=True) 

class languageModel(models.Model):
    proficiency_level_choices=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('expert','Expert'),
    ]
    user=models.ForeignKey(customUser,null=True,on_delete=models.CASCADE)
    language_name=models.CharField(max_length=100,null=True)
    proficiency=models.CharField(max_length=100,null=True) 

class Meta:
    uniquc_together=['user','language_name'] 

def __str__(self)->str:
    return self.user.username+''+self.language_name

class IntermediateModel(models.Model):
    language_name=models.CharField(max_length=100,null=True)
    def __str__(self)->str:
      return self.language_name

