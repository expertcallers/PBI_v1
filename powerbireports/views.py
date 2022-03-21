from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .models import *


def view_404(request, exception=None): 
    return render(request,'404.html')
    
# login-page
def loginPage(request):
    logout(request)
    return render(request, 'login.html')


def loginAndRedirect(request):
    if request.method == 'POST':
        username = request.POST["user"]
        password = request.POST["pass"]
        user = authenticate(username=username, password=password)

        if user is not None:
            # user_login
            login(request, user)
            # for getting campaignid
            campaiginid = request.user.profile.campaignid

            # this is for manager's login
            if campaiginid == 'all':
                return redirect('/pbireport/management-dashboard')

            # this is for other reports login
            else:
                return redirect('/pbireport/report/'+campaiginid)

        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Invalid Password !')
            else:
                messages.info(request, 'Invalid Username and Password !')
            return render(request, 'login.html')

    else:
        logout(request)
        return render(request, 'login.html')


def logoutNew(request):
    logout(request)
    return render(request, 'login.html')


# Management Dashboard
@login_required
def managementDashboard(request):
    if request.user.profile.campaignid == 'all':
        all_cam = Profile.objects.exclude(campaign_type=None).count()
        outbound = Profile.objects.filter(campaign_type="Outbound").count()
        inbound = Profile.objects.filter(campaign_type="Inbound").count()
        email = Profile.objects.filter(campaign_type="Email").count()
        other = Profile.objects.filter(campaign_type="Other").count()
        data = {"all": all_cam, "outbound": outbound, "inbound": inbound, "email": email, "other": other}
        return render(request, 'management_dashboard.html', data)
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/')

@login_required
def campaignsReport(request,type):
    if request.user.profile.campaignid == 'all':
        if type == "all":
            pro = Profile.objects.exclude(campaign_type=None)
        else:
            pro = Profile.objects.filter(campaign_type=type)
        data = {'profile': pro,"type":type}
        return render(request, 'reports_all.html', data)
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')

            user = request.user
            user.profile.pc = True
            user.save()
            user.profile.save()
            logout(request)
            return redirect('/pbireport/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'settings.html', {'form': form})


@login_required
def allReport(request,cid):
    if request.user.profile.campaignid == cid or request.user.profile.campaignid == 'all':
        if request.user.profile.campaign_status == False:
            messages.info(request, "The Campaign is currently paused")
            return redirect('/pbireport/')
        else:
            return render(request, ''+cid+'.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/')
