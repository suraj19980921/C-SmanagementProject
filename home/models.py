from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class College(models.Model):

    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    college_name = models.CharField( max_length=100)
    college_address = models.CharField( max_length=200)
    college_phone = models.BigIntegerField()
    college_description = models.CharField(max_length=500)

