from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .models import *


# Create your views here.
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
            if campaiginid == '0001':
                return redirect('/pbireport/bigo-reports')

            if campaiginid == '0002':
                return redirect('/pbireport/aadya-reports')

            if campaiginid == '0003':
                return redirect('/pbireport/aditya-birla-cellulose-reports')

            if campaiginid == '0004':
                return redirect('/pbireport/aditya-birla-toll-free-reports')

            if campaiginid == '0005':
                return redirect('/pbireport/aditya-birla-nps-reports')

            if campaiginid == '0006':
                return redirect('/pbireport/aditya-birla-retailer-calling-nps-reports')

            if campaiginid == '0007':
                return redirect('/pbireport/aditya-birla-website-enquiry-reports')

            if campaiginid == '0008':
                return redirect('/pbireport/akdy-calls')

            if campaiginid == '0009':
                return redirect('/pbireport/avenue-living-communities')

            if campaiginid == '0010':
                return redirect('/pbireport/bhagyalaxmi-industries')

            if campaiginid == '0011':
                return redirect('/pbireport/bng-vs-php')

            if campaiginid == '0012':
                return redirect('/pbireport/career-transition-specialist')

            if campaiginid == '0013':
                return redirect('/pbireport/citizen-capital')

            if campaiginid == '0014':
                return redirect('/pbireport/core-small-insurance-agency-inc')

            if campaiginid == '0015':
                return redirect('/pbireport/cross-tower')

            if campaiginid == '0016':
                return redirect('/pbireport/csc-service-works')

            if campaiginid == '0017':
                return redirect('/pbireport/daniel-wellington')

            if campaiginid == '0018':
                return redirect('/pbireport/digital-signage')

            if campaiginid == '0019':
                return redirect('/pbireport/digital-swiss-gold')

            if campaiginid == '0020':
                return redirect('/pbireport/ee-hh-aaa')

            if campaiginid == '0021':
                return redirect('/pbireport/embassy-premium')

            if campaiginid == '0022':
                return redirect('/pbireport/fame-house')

            if campaiginid == '0023':
                return redirect('/pbireport/fitness-mortgage')

            if campaiginid == '0024':
                return redirect('/pbireport/genesis-acquisition')

            if campaiginid == '0025':
                return redirect('/pbireport/golden-eye-cctv')

            if campaiginid == '0026':
                return redirect('/pbireport/gubagoo')

            if campaiginid == '0027':
                return redirect('/pbireport/hindalco')

            if campaiginid == '0028':
                return redirect('/pbireport/ilm')

            if campaiginid == '0029':
                return redirect('/pbireport/imaginarium')

            if campaiginid == '0030':
                return redirect('/pbireport/imprint-plus')

            if campaiginid == '0031':
                return redirect('/pbireport/insalvage')

            if campaiginid == '0032':
                return redirect('/pbireport/kaapi-machines')

            if campaiginid == '0033':
                return redirect('/pbireport/lawoffice-m-geller')

            if campaiginid == '0034':
                return redirect('/pbireport/marcelo-perez')

            if campaiginid == '0035':
                return redirect('/pbireport/marin-rv-storage')

            if campaiginid == '0036':
                return redirect('/pbireport/medicare')

            if campaiginid == '0037':
                return redirect('/pbireport/mob-twenty-two')

            if campaiginid == '0038':
                return redirect('/pbireport/monster-lead')

            if campaiginid == '0039':
                return redirect('/pbireport/movement-insurance')

            if campaiginid == '0040':
                return redirect('/pbireport/naffa-innovations')

            if campaiginid == '0041':
                return redirect('/pbireport/new-dim-pharmacy')

            if campaiginid == '0042':
                return redirect('/pbireport/noom')

            if campaiginid == '0043':
                return redirect('/pbireport/printer-pix')

            if campaiginid == '0044':
                return redirect('/pbireport/protostar')

            if campaiginid == '0045':
                return redirect('/pbireport/rainbow-dia-lts')

            if campaiginid == '0046':
                return redirect('/pbireport/sana-life-science')

            if campaiginid == '0047':
                return redirect('/pbireport/saura-khalki-fashion')

            if campaiginid == '0048':
                return redirect('/pbireport/schindler-media')

            if campaiginid == '0049':
                return redirect('/pbireport/somethings-brewing')

            if campaiginid == '0050':
                return redirect('/pbireport/sterling-strategies-llc')

            if campaiginid == '0051':
                return redirect('/pbireport/tanaor-jewelry-lsrael-ltd')

            if campaiginid == '0052':
                return redirect('/pbireport/tca-counseling-group')

            if campaiginid == '0053':
                return redirect('/pbireport/tech-report')

            if campaiginid == '0054':
                return redirect('/pbireport/us-jaclean-inc')

            if campaiginid == '0055':
                return redirect('/pbireport/ups-nps')

            if campaiginid == '0056':
                return redirect('/pbireport/window-treatment-unlimited')

            if campaiginid == '0057':
                return redirect('/pbireport/winopoly')

            if campaiginid == '0058':
                return redirect('/pbireport/practo')

            if campaiginid == "0059":
                return redirect('/pbireport/allcare-phycical')

            if campaiginid == "0060":
                return redirect('/pbireport/blazing-hog')

            if campaiginid == "0061":
                return redirect('/pbireport/bright-way')

            if campaiginid == "0062":
                return redirect('/pbireport/calista')

            if campaiginid == "0063":
                return redirect('/pbireport/global-arc')

            if campaiginid == "0064":
                return redirect('/pbireport/jiffy-ship-cargo')

            if campaiginid == "0065":
                return redirect('/pbireport/pick-pack-delivery')

            if campaiginid == "0066":
                return redirect('/pbireport/sapphire-medicals')

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
        all_cam = Profile.objects.all().exclude(campaign_type=None).count()
        outbound = Profile.objects.filter(campaign_type="Outbound").count()
        inbound = Profile.objects.filter(campaign_type="Inbound").count()
        email = Profile.objects.filter(campaign_type="Email").count()
        other = Profile.objects.filter(campaign_type="Other").count()
        data = {"all": all_cam, "outbound": outbound, "inbound": inbound, "email": email, "other": other}
        return render(request, 'management_dashboard.html', data)
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')

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
        return redirect('/pbireport/logout')

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


# bigo-report
@login_required
def bigoReport(request):
    if request.user.profile.campaignid == '0001' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_bigo.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# aadya-reports
@login_required
def aadyaReport(request):
    if request.user.profile.campaignid == '0002' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aadya.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# aditya-birla-cellulose-reports
@login_required
def adityaBirlaCelluloseReport(request):
    if request.user.profile.campaignid == '0003' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_ab_cellulose.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# aditya-birla-toll-free-reports
@login_required
def adityaBirlaTollFreeReport(request):
    if request.user.profile.campaignid == '0004' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_ab_toll_free.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# aditya-birla-nps-reports
@login_required
def adityaBirlaNPSReport(request):
    if request.user.profile.campaignid == '0005' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aditya_birla_nps.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# aditya-birla-retailer-calling-nps-reports
@login_required
def adityaBirlaRetailerCallingReport(request):
    if request.user.profile.campaignid == '0006' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aditya_birla_retailer_calling.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# aditya-birla-website-enquiry-reports
@login_required
def adityaBirlaWebsiteEnquiryReport(request):
    if request.user.profile.campaignid == '0007' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aditya_birla_website_enquiry.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# akdy-calls
@login_required
def aKDYcallsReport(request):
    if request.user.profile.campaignid == '0008' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_akdy.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# avenue-living-communities
@login_required
def avenueLivingCommunitiesReport(request):
    if request.user.profile.campaignid == '0009' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_avenue_living_communities.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# bhagyalaxmi-industries
@login_required
def bhagyalaxmiIndustriespractoReport(request):
    if request.user.profile.campaignid == '0010' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_bhagyalaxmi_industries.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# bng-vs-php
@login_required
def bNGvsPHPreport(request):
    if request.user.profile.campaignid == '0011' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_BNG_Vs_PHP.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# career-transition-specialist
@login_required
def careerTransitionSpecialistReport(request):
    if request.user.profile.campaignid == '0012' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Career_Transition_Specialist.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# citizen-capital
@login_required
def citizenCapitalReport(request):
    if request.user.profile.campaignid == '0013' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Citizen_Capital.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# core-small-insurance-agency-inc
@login_required
def coreySmallInsuranceAgencyIncReport(request):
    if request.user.profile.campaignid == '0014' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Corey_Small_Insurance_Agency_Inc.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# cross-tower
@login_required
def crossTowerReport(request):
    if request.user.profile.campaignid == '0015' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Cross_Tower.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# csc-service-works
@login_required
def cSCserviceWorksReport(request):
    if request.user.profile.campaignid == '0016' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_CSC_Service_Works.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# daniel-wellington
@login_required
def danielWellingtonReport(request):
    if request.user.profile.campaignid == '0017' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Daniel_Wellington.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# digital-signage
@login_required
def digitalSignageReport(request):
    if request.user.profile.campaignid == '0018' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Digital_Signage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# digital-swiss-gold
@login_required
def digitalSwissGoldReport(request):
    if request.user.profile.campaignid == '0019' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Digital_Swiss_Gold.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# ee-hh-aaa
@login_required
def eEHHAAAreport(request):
    if request.user.profile.campaignid == '0020' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_EEHHAAA.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# embassy-premium
@login_required
def embassyPremiumReport(request):
    if request.user.profile.campaignid == '0021' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Embassy_Premium.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# fame-house
@login_required
def fameHouseReport(request):
    if request.user.profile.campaignid == '0022' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Fame_House.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# fitness-mortgage
@login_required
def fitnessMortgageReport(request):
    if request.user.profile.campaignid == '0023' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Finesse_Mortgage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# genesis-acquisition
@login_required
def genesisAccquisitionReport(request):
    if request.user.profile.campaignid == '0024' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Genesis_Acquisition.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# golden-eye-cctv
@login_required
def goldenEyeCCTVreport(request):
    if request.user.profile.campaignid == '0025' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Golden_Eye_CCTV.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# gubagoo
@login_required
def gUbagooReport(request):
    if request.user.profile.campaignid == '0026' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Gubagoo.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# hindalco
@login_required
def hindalcoReport(request):
    if request.user.profile.campaignid == '0027' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Hindalco.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# ilm
@login_required
def iLMreport(request):
    if request.user.profile.campaignid == '0028' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_ILM.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# imaginarium
@login_required
def imaginariumSolutionsLTDreport(request):
    if request.user.profile.campaignid == '0029' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Imaginarium_Solutions_Ltd.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# imprint-plus
@login_required
def imprintPlusReport(request):
    if request.user.profile.campaignid == '0030' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Imprint_Plus.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# insalvage
@login_required
def iNsalvageReport(request):
    if request.user.profile.campaignid == '0031' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Insalvage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# kaapi-machines
@login_required
def kaapiMachinesReport(request):
    if request.user.profile.campaignid == '0032' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Kaapi_Machines.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# lawoffice-m-geller
@login_required
def lawOfficesRobertMgellerReport(request):
    if request.user.profile.campaignid == '0033' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_LAW_OFFICES_OF_ROBERT_M._GELLER.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# marcelo-perez
@login_required
def marceloPerezStateFarmReport(request):
    if request.user.profile.campaignid == '0034' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_MARCELO_PEREZ_STATE_FARM.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# marin-rv-storage
@login_required
def marinRVstorageReport(request):
    if request.user.profile.campaignid == '0035' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Marin_RV_Storage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# medicare
@login_required
def mediCareReport(request):
    if request.user.profile.campaignid == '0036' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Medicare.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# mob-twenty-two
@login_required
def mobileTwentyTwoReport(request):
    if request.user.profile.campaignid == '0037' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Mobile_22.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# monster-lead
@login_required
def monsterLeadReport(request):
    if request.user.profile.campaignid == '0038' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Monster_Lead.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# movement-insurance
@login_required
def movementInsuranceReport(request):
    if request.user.profile.campaignid == '0039' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Movement_Insurance.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# naffa-innovations
@login_required
def naffaInnovationsReport(request):
    if request.user.profile.campaignid == '0040' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Naffa_Innovations.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# new-dim-pharmacy
@login_required
def newDimensionPharmacyReport(request):
    if request.user.profile.campaignid == '0041' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_New_Dimension_Pharmacy.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# noom
@login_required
def noomReport(request):
    if request.user.profile.campaignid == '0042' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Noom.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# printer-pix
@login_required
def printerPixReport(request):
    if request.user.profile.campaignid == '0043' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Printerpix.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# protostar
@login_required
def protostarReport(request):
    if request.user.profile.campaignid == '0044' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Protostar.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# rainbow-dia-lts
@login_required
def rainbowDiagnosticsLTSreport(request):
    if request.user.profile.campaignid == '0045' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_RainBow_Diagnostics_LTS.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# sana-life-science
@login_required
def sanaLifeScienceReport(request):
    if request.user.profile.campaignid == '0046' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Sana_Life_Science.html')
    else:

        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# saura-khalki-fashion
@login_required
def saurabhaktiKhalkiFasionReport(request):
    if request.user.profile.campaignid == '0047' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Saurabhakti_Khalki_Fashion.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# schindler-media
@login_required
def schindlerMediaReport(request):
    if request.user.profile.campaignid == '0048' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Schindler_Media.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# somethings-brewing
@login_required
def somethingsBrewingReport(request):
    if request.user.profile.campaignid == '0049' or request.user.profile.campaignid == 'all':
        return render(request, "reports_Something's_Brewing.html")
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# sterling-strategies-llc
@login_required
def sterlingStrategiesLLCreport(request):
    if request.user.profile.campaignid == '0050' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Sterling_Strategies_Llc.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# tanaor-jewelry-lsrael-ltd
@login_required
def tanaorJewelryIsraelLtdReport(request):
    if request.user.profile.campaignid == '0051' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Tanaor_Jewelry_Israel_Ltd.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# tca-counseling-group
@login_required
def tCAcounselingGroupReport(request):
    if request.user.profile.campaignid == '0052' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_TCA_Counseling_Group.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# tech-report
@login_required
def techReport(request):
    if request.user.profile.campaignid == '0053' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Tech_Report.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# us-jaclean-inc
@login_required
def uSJacleanINCreport(request):
    if request.user.profile.campaignid == '0054' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_U_S_JACLEAN_INC.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# ups-nps
@login_required
def uPSNPSreport(request):
    if request.user.profile.campaignid == '0055' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_UPS_NPS.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# window-treatment-unlimited
@login_required
def windowTreatmentUnlimitedReport(request):
    if request.user.profile.campaignid == '0056' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Window_Treatment_Unlimited.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# winopoly
@login_required
def winopolyReport(request):
    if request.user.profile.campaignid == '0057' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Winopoly.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# Practo
@login_required
def PractoReport(request):
    if request.user.profile.campaignid == '0058' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Practo_Technologies_Cumulative.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')

# All Care Physical Therapy
@login_required
def allCarePhysicalTherapy(request):
    if request.user.profile.campaignid == '0059' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_all_care_physical_therapy.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# blazing-hog
@login_required
def blazingHogAndWahooInternet(request):
    if request.user.profile.campaignid == '0060' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_blazing_hog.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')

# bright-way
@login_required
def brightWay(request):
    if request.user.profile.campaignid == '0061' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_bright_way.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


# calista
@login_required
def Calista(request):
    if request.user.profile.campaignid == '0062' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Calista.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')

# global-arc
@login_required
def globalARC(request):
    if request.user.profile.campaignid == '0063' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_global_arc.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')

# jiffy-ship-cargo
@login_required
def jiffyShipCargo(request):
    if request.user.profile.campaignid == '0064' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Jiffy_Ship_Cargo.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')

# pick-pack-delivery
@login_required
def pickPackDelivery(request):
    if request.user.profile.campaignid == '0065' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Pick_Pack_Delivery.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')

# sapphire-medicals
@login_required
def sapphireMedicals(request):
    if request.user.profile.campaignid == '0066' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Sapphire_Medicals.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/pbireport/logout')


@login_required
def mgtReport(request, cid):
    campaiginid = cid

    if campaiginid == '0001':
        return redirect('/pbireport/bigo-reports')

    if campaiginid == '0002':
        return redirect('/pbireport/aadya-reports')

    if campaiginid == '0003':
        return redirect('/pbireport/aditya-birla-cellulose-reports')

    if campaiginid == '0004':
        return redirect('/pbireport/aditya-birla-toll-free-reports')

    if campaiginid == '0005':
        return redirect('/pbireport/aditya-birla-nps-reports')

    if campaiginid == '0006':
        return redirect('/pbireport/aditya-birla-retailer-calling-nps-reports')

    if campaiginid == '0007':
        return redirect('/pbireport/aditya-birla-website-enquiry-reports')

    if campaiginid == '0008':
        return redirect('/pbireport/akdy-calls')

    if campaiginid == '0009':
        return redirect('/pbireport/avenue-living-communities')

    if campaiginid == '0010':
        return redirect('/pbireport/bhagyalaxmi-industries')

    if campaiginid == '0011':
        return redirect('/pbireport/bng-vs-php')

    if campaiginid == '0012':
        return redirect('/pbireport/career-transition-specialist')

    if campaiginid == '0013':
        return redirect('/pbireport/citizen-capital')

    if campaiginid == '0014':
        return redirect('/pbireport/core-small-insurance-agency-inc')

    if campaiginid == '0015':
        return redirect('/pbireport/cross-tower')

    if campaiginid == '0016':
        return redirect('/pbireport/csc-service-works')

    if campaiginid == '0017':
        return redirect('/pbireport/daniel-wellington')

    if campaiginid == '0018':
        return redirect('/pbireport/digital-signage')

    if campaiginid == '0019':
        return redirect('/pbireport/digital-swiss-gold')

    if campaiginid == '0020':
        return redirect('/pbireport/ee-hh-aaa')

    if campaiginid == '0021':
        return redirect('/pbireport/embassy-premium')

    if campaiginid == '0022':
        return redirect('/pbireport/fame-house')

    if campaiginid == '0023':
        return redirect('/pbireport/fitness-mortgage')

    if campaiginid == '0024':
        return redirect('/pbireport/genesis-acquisition')

    if campaiginid == '0025':
        return redirect('/pbireport/golden-eye-cctv')

    if campaiginid == '0026':
        return redirect('/pbireport/gubagoo')

    if campaiginid == '0027':
        return redirect('/pbireport/hindalco')

    if campaiginid == '0028':
        return redirect('/pbireport/ilm')

    if campaiginid == '0029':
        return redirect('/pbireport/imaginarium')

    if campaiginid == '0030':
        return redirect('/pbireport/imprint-plus')

    if campaiginid == '0031':
        return redirect('/pbireport/insalvage')

    if campaiginid == '0032':
        return redirect('/pbireport/kaapi-machines')

    if campaiginid == '0033':
        return redirect('/pbireport/lawoffice-m-geller')

    if campaiginid == '0034':
        return redirect('/pbireport/marcelo-perez')

    if campaiginid == '0035':
        return redirect('/pbireport/marin-rv-storage')

    if campaiginid == '0036':
        return redirect('/pbireport/medicare')

    if campaiginid == '0037':
        return redirect('/pbireport/mob-twenty-two')

    if campaiginid == '0038':
        return redirect('/pbireport/monster-lead')

    if campaiginid == '0039':
        return redirect('/pbireport/movement-insurance')

    if campaiginid == '0040':
        return redirect('/pbireport/naffa-innovations')

    if campaiginid == '0041':
        return redirect('/pbireport/new-dim-pharmacy')

    if campaiginid == '0042':
        return redirect('/pbireport/noom')

    if campaiginid == '0043':
        return redirect('/pbireport/printer-pix')

    if campaiginid == '0044':
        return redirect('/pbireport/protostar')

    if campaiginid == '0045':
        return redirect('/pbireport/rainbow-dia-lts')

    if campaiginid == '0046':
        return redirect('/pbireport/sana-life-science')

    if campaiginid == '0047':
        return redirect('/pbireport/saura-khalki-fashion')

    if campaiginid == '0048':
        return redirect('/pbireport/schindler-media')

    if campaiginid == '0049':
        return redirect('/pbireport/somethings-brewing')

    if campaiginid == '0050':
        return redirect('/pbireport/sterling-strategies-llc')

    if campaiginid == '0051':
        return redirect('/pbireport/tanaor-jewelry-lsrael-ltd')

    if campaiginid == '0052':
        return redirect('/pbireport/tca-counseling-group')

    if campaiginid == '0053':
        return redirect('/pbireport/tech-report')

    if campaiginid == '0054':
        return redirect('/pbireport/us-jaclean-inc')

    if campaiginid == '0055':
        return redirect('/pbireport/ups-nps')

    if campaiginid == '0056':
        return redirect('/pbireport/window-treatment-unlimited')

    if campaiginid == '0057':
        return redirect('/pbireport/winopoly')

    if campaiginid == '0058':
        return redirect('/pbireport/practo')

    if campaiginid == "0059":
        return redirect('/pbireport/allcare-phycical')

    if campaiginid == "0060":
        return redirect('/pbireport/blazing-hog')

    if campaiginid == "0061":
        return redirect('/pbireport/bright-way')

    if campaiginid == "0062":
        return redirect('/pbireport/calista')

    if campaiginid == "0063":
        return redirect('/pbireport/global-arc')

    if campaiginid == "0064":
        return redirect('/pbireport/jiffy-ship-cargo')

    if campaiginid == "0065":
        return redirect('/pbireport/pick-pack-delivery')

    if campaiginid == "0066":
        return redirect('/pbireport/sapphire-medicals')

