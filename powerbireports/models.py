from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    campaign = models.CharField(max_length=200)
    campaignid = models.CharField(max_length=200)
    campaign_type = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.campaign

