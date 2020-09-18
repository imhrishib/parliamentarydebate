from django.db import models

# Create your models here.

class teams(models.Model):
    name1=models.CharField(max_length=100)
    name2=models.CharField(max_length=100)
    name3=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    contactno=models.CharField(max_length=10,unique=True)
    
    def __str__(self):
        return self.name1

class adjudicators(models.Model):
    name=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    contactno=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name
