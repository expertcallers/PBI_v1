from django.contrib import admin
from .models import *
# Register your models here.
class Search(admin.ModelAdmin):
    search_fields = ("campaignid","campaign", 'campaign_type')
    list_display = ('campaignid',"campaign", 'campaign_type','user','campaign_status')
admin.site.register(Profile,Search)
