from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/login/',loginPage),
    path('', loginPage),
    path('logout', logoutNew),
    path('login',loginAndRedirect),
    path('management-dashboard',managementDashboard),
    path('campaigns/<str:type>', campaignsReport),
    path('report/<str:cid>', allReport),
    path('management',managementDashboard),
    path('settings', change_password),
    path('change-password', forceChangePassword),

    path('campaign-assigning', campaignAssigning),
    path('delete-mapping', deleteMapping),
    path('create-users', createUsers),
]