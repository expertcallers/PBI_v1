from django.contrib import admin
from .models import *
# Register your models here.
class Search(admin.ModelAdmin):
    search_fields = ("campaign", 'campaign_type')
    list_display = ('campaignid',"campaign", 'campaign_type','user')
admin.site.register(Profile,Search)
