from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


# Register your models here.


class profileSearchResource(resources.ModelResource):
    class Meta:
        model = Profile

class Search(ImportExportModelAdmin):
    search_fields = ("campaignid", "campaign", 'user')
    list_display = ('campaignid', "campaign", 'campaign_type', 'user', 'campaign_status')
    list_filter = ['campaign_type']
    resource_class = profileSearchResource


class MappingSearchResource(resources.ModelResource):
    class Meta:
        model = Mapping

class MappingSearch(ImportExportModelAdmin):
    search_fields = ("campaign", "user")
    list_display = ('user', "campaign")
    resource_class = MappingSearchResource


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

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('username', 'id')

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ("id", "username",)
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, Search)
admin.site.register(Mapping, MappingSearch)
admin.site.register(Employees, EmployeesSearch)
