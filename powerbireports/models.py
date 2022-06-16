from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    campaign = models.CharField(max_length=200)
    campaignid = models.CharField(max_length=200)
    campaign_type = models.CharField(max_length=50,blank=True,null=True)
    campaign_status = models.BooleanField(default=True)
    pc = models.BooleanField(default=False)

    def __str__(self):
        return self.campaign +" - "+ self.campaignid

class Mapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Employees(models.Model):
    emp_id = models.CharField(max_length=30)
    emp_name = models.CharField(max_length=200)
    emp_desi = models.CharField(max_length=200)
