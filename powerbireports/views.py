from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .models import *

manager_list = ['TA Manager', 'Operations Manager', 'IT Manager', 'Associate Director', 'Vice President',
                'Learning and Development Head', 'Chief Compliance Officer', 'Chief Executive Officer',
                'Managing Director', 'HR Manager', 'Board member', 'Command Centre Head', 'Chief Technology Officer']

def view_404(request, exception=None): 
    return render(request,'404.html')
    
# login-page
def loginPage(request):
    if request.user.is_authenticated:
        campaiginid = request.user.profile.campaignid
        if campaiginid == 'all':
            return redirect('/pbireport/management-dashboard')
        else:
            return redirect('/pbireport/report/' + campaiginid)
    else:
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
            pc = request.user.profile.pc
            if pc == False:
                return redirect('/pbireport/change-password')

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
            return redirect('/pbireport/')

    else:
        logout(request)
        return redirect('/pbireport/')


def logoutNew(request):
    logout(request)
    return render(request, 'login.html')


# Management Dashboard
@login_required
def managementDashboard(request):
    campaignid = request.user.profile.campaignid
    campaign_type = request.user.profile.campaign_type
    if campaignid == 'all':
        if campaign_type == 'limited':
            cam_id = []
            mapping = Mapping.objects.filter(user=request.user)
            for i in mapping:
                cam_id.append(i.campaign.campaignid)
            all_cam = Profile.objects.filter(campaignid__in=cam_id).exclude(
                Q(campaign_type=None) | Q(campaign_type='limited')).count()
        else:
            all_cam = Profile.objects.exclude(Q(campaign_type=None) | Q(campaign_type='limited')).count()

        if campaign_type == 'limited':
            cam_id = []
            mapping = Mapping.objects.filter(user=request.user)
            for i in mapping:
                cam_id.append(i.campaign.campaignid)
            outbound = Profile.objects.filter(campaignid__in=cam_id, campaign_type="Outbound").count()
        else:
            outbound = Profile.objects.filter(campaign_type="Outbound").count()

        if campaign_type == 'limited':
            cam_id = []
            mapping = Mapping.objects.filter(user=request.user)
            for i in mapping:
                cam_id.append(i.campaign.campaignid)
            inbound = Profile.objects.filter(campaignid__in=cam_id, campaign_type="Inbound").count()
        else:
            inbound = Profile.objects.filter(campaign_type="Inbound").count()

        if campaign_type == 'limited':
            cam_id = []
            mapping = Mapping.objects.filter(user=request.user)
            for i in mapping:
                cam_id.append(i.campaign.campaignid)
            email = Profile.objects.filter(campaignid__in=cam_id, campaign_type="Email").count()
        else:
            email = Profile.objects.filter(campaign_type="Email").count()

        if campaign_type == 'limited':
            cam_id = []
            mapping = Mapping.objects.filter(user=request.user)
            for i in mapping:
                cam_id.append(i.campaign.campaignid)
            other = Profile.objects.filter(campaignid__in=cam_id, campaign_type="Other").count()
        else:
            other = Profile.objects.filter(campaign_type="Other").count()

        data = {"all": all_cam, "outbound": outbound, "inbound": inbound, "email": email, "other": other}
        return render(request, 'management_dashboard.html', data)
    else:
        messages.info(request, "Bad Request.")
        return redirect('/pbireport/')

@login_required
def campaignsReport(request,type):
    campaignid = request.user.profile.campaignid
    campaign_type = request.user.profile.campaign_type
    if campaignid == 'all':
        if type == "all":
            if campaign_type == 'limited':
                cam_id = []
                mapping = Mapping.objects.filter(user=request.user)
                for i in mapping:
                    cam_id.append(i.campaign.campaignid)
                pro = Profile.objects.filter(campaignid__in=cam_id).exclude(Q(campaign_type=None) | Q(campaign_type='limited'))
            else:
                pro = Profile.objects.exclude(Q(campaign_type=None) | Q(campaign_type='limited'))
        else:
            if campaign_type == 'limited':
                cam_id = []
                mapping = Mapping.objects.filter(user=request.user)
                for i in mapping:
                    cam_id.append(i.campaign.campaignid)
                pro = Profile.objects.filter(campaign_type=type, campaignid__in=cam_id).exclude(campaign_type=None)
            else:
                pro = Profile.objects.filter(campaign_type=type)
        data = {'profile': pro,"type":type}
        return render(request, 'reports_all.html', data)
    else:
        messages.info(request, "Bad Request!")
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
def forceChangePassword(request):
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
    return render(request, 'password.html', {'form': form})

@login_required
def allReport(request,cid):
    campaignid = request.user.profile.campaignid
    campaign_type = request.user.profile.campaign_type
    if campaignid == cid or campaignid == 'all':
        if request.user.profile.campaign_status == False:
            messages.info(request, "The Campaign is currently paused")
            return redirect('/pbireport/')
        elif campaign_type == 'limited':
            cam_id = []
            mapping = Mapping.objects.filter(user=request.user)
            for i in mapping:
                cam_id.append(i.campaign.campaignid)
            if cid in cam_id:
                return render(request, '' + cid + '.html')
            else:
                messages.info(request, "Bad Request!")
                return redirect('/pbireport/')
        else:
            return render(request, ''+cid+'.html')
    else:
        messages.info(request, "Bad Request!")
        return redirect('/pbireport/')


@login_required
def campaignAssigning(request):
    if request.user.profile.campaign_type == None:
        if request.method == "POST":
            user = request.POST['user']
            user = User.objects.get(username=user)
            campaign = request.POST['campaign']
            campaign = Profile.objects.get(campaignid=campaign)
            Mapping.objects.create(user=user, campaign=campaign)
            return redirect('/pbireport/campaign-assigning')

        else:
            campaigns = Profile.objects.exclude(Q(campaign_type=None) | Q(campaign_type='limited'))
            profiles = Profile.objects.filter(Q(campaign_type='limited'))
            mapping = Mapping.objects.all()
            mapping_list = []
            for i in mapping:
                dic = {}
                profile = Profile.objects.get(user=i.user)
                dic['user'] = profile.campaign+" ("+str(i.user)+")"
                dic['campaign'] = i.campaign
                dic['id'] = i.id
                mapping_list.append(dic)
            data = {'campaigns':campaigns, 'profiles':profiles, 'mapping':mapping_list}
            return render(request, 'superadmin/campaign_assigning.html', data)
    else:
        messages.info(request, "Bad Request!")
        return redirect('/pbireport/')

@login_required
def deleteMapping(request):
    if request.method == "POST":
        id = request.POST['id']
        Mapping.objects.get(id=id).delete()
        return redirect('/pbireport/campaign-assigning')
    else:
        messages.info(request, "Bad Request!")
        return redirect('/pbireport/')

def createUsers(request):
    employees = Employees.objects.all()
    for i in employees:
        user = User.objects.filter(username=i.emp_id)
        if user.exists():
            try:
                for i in user:
                    user = i
                Profile.objects.get(user=user)
            except:
                if i.emp_desi in manager_list:
                    Profile.objects.create(
                        user=user, campaign=i.emp_name, campaignid='all',
                    )
                else:
                    Profile.objects.create(
                        user=user, campaign=i.emp_name, campaignid='all', campaign_type='limited',
                    )
        else:
            user = User.objects.create_user(username=i.emp_id, password=str(i.emp_id))
            if i.emp_desi in manager_list:
                Profile.objects.create(
                    user=user, campaign=i.emp_name, campaignid='all',
                )
            else:
                Profile.objects.create(
                    user=user, campaign=i.emp_name, campaignid='all', campaign_type='limited',
                )
    return redirect('/')