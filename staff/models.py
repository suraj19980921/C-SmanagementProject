from django.db import models
from home.models import College

# Create your models here.

class Staff(models.Model):

    college = models.ForeignKey(College,default=None,on_delete=models.CASCADE)
    staff_name = models.CharField( max_length=100)
    staff_address = models.CharField( max_length=200)
    staff_phone = models.BigIntegerField()
    staff_description = models.CharField(max_length=500)

