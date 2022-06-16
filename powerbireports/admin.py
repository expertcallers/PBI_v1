from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


# Register your models here.
class Search(admin.ModelAdmin):
    search_fields = ("campaignid", "campaign", 'user')
    list_display = ('campaignid', "campaign", 'campaign_type', 'user', 'campaign_status')
    list_filter = ['campaign_type']


class MappingSearch(admin.ModelAdmin):
    search_fields = ("campaign", "user")
    list_display = ('user', "campaign")


class EmployeesSearchResource(resources.ModelResource):
    class Meta:
        model = Employees
        fields = ["emp_id", "emp_name", "emp_desi"]
        import_id_fields = ('emp_id',)


class EmployeesSearch(ImportExportModelAdmin):
    search_fields = ("emp_id", "emp_name", "emp_desi")
    list_display = ("emp_id", "emp_name", "emp_desi")
    list_filter = ['emp_desi']
    resource_class = EmployeesSearchResource


admin.site.register(Profile, Search)
admin.site.register(Mapping, MappingSearch)
admin.site.register(Employees, EmployeesSearch)
