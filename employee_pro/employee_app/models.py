from django.db import models

# Create your models here.
class Employee(models.Model):
    empno= models.IntegerField()
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    salary= models.IntegerField()
    location= models.CharField(max_length=50)
    company= models.CharField(max_length=50)
    position= models.CharField(max_length=50)
    mobile= models.BigIntegerField()
    email= models.EmailField(max_length=50)

