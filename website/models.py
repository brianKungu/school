from django.db import models
from django.shortcuts import reverse

# Create your models here.
class About(models.Model):
    motto=models.CharField(max_length=500)
    logo=models.FileField()
    mission=models.CharField(max_length=500)
    vision=models.CharField(max_length=500)
    def get_absolute_url(self):
        return reverse('website:index')
class Club(models.Model):
    club_name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    patron=models.CharField(max_length=100)

class Department(models.Model):
    department_name=models.CharField(max_length=100)
    department_head=models.CharField(max_length=100)
    sub_head=models.CharField(max_length=100)

class Staff(models.Model):
    staff_name=models.CharField(max_length=100)
    id_number=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    role=models.CharField(max_length=100)

