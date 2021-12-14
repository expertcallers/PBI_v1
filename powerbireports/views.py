# from pyexpat.errors import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import *


# Create your views here.
# login-page
def loginPage(request):
    return render(request,'login.html')

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

            if campaiginid == '0001':
                return redirect('/bigo-reports')


            if campaiginid == '0002':
                return redirect('/aadya-reports')

            if campaiginid == '0003':
                return redirect('/aditya-birla-cellulose-reports')

            if campaiginid == '0004':
                return redirect('/aditya-birla-toll-free-reports')

            if campaiginid == '0005':
                return redirect('/aditya-birla-nps-reports')

            if campaiginid == '0006':
                return redirect('/aditya-birla-retailer-calling-nps-reports')

            if campaiginid == '0007':
                return redirect('/aditya-birla-website-enquiry-reports')

            if campaiginid == '0008':
                return redirect('/akdy-calls')

            if campaiginid == '0009':
                return redirect('/avenue-living-communities')

            if campaiginid == '0010':
                return redirect('/bhagyalaxmi-industries')

            if campaiginid == '0011':
                return redirect('/bng-vs-php')

            if campaiginid == '0012':
                return redirect('/career-transition-specialist')

            if campaiginid == '0013':
                return redirect('/citizen-capital')

            if campaiginid == '0014':
                return redirect('/core-small-insurance-agency-inc')

            if campaiginid == '0015':
                return redirect('/cross-tower')

            if campaiginid == '0016':
                return redirect('/csc-service-works')

            if campaiginid == '0017':
                return redirect('/daniel-wellington')

            if campaiginid == '0018':
                return redirect('/digital-signage')

            if campaiginid == '0019':
                return redirect('/digital-swiss-gold')

            if campaiginid == '0020':
                return redirect('/ee-hh-aaa')

            if campaiginid == '0021':
                return redirect('/embassy-premium')

            if campaiginid == '0022':
                return redirect('/fame-house')

            if campaiginid == '0023':
                return redirect('/fitness-mortgage')

            if campaiginid == '0024':
                return redirect('/genesis-acquisition')

            if campaiginid == '0025':
                return redirect('/golden-eye-cctv')

            if campaiginid == '0026':
                return redirect('/gubagoo')

            if campaiginid == '0027':
                return redirect('/hindalco')

            if campaiginid == '0028':
                return redirect('/ilm')

            if campaiginid == '0029':
                return redirect('/imaginarium')

            if campaiginid == '0030':
                return redirect('/imprint-plus')

            if campaiginid == '0031':
                return redirect('/insalvage')

            if campaiginid == '0032':
                return redirect('/kaapi-machines')

            if campaiginid == '0033':
                return redirect('/lawoffice-m-geller')

            if campaiginid == '0034':
                return redirect('/marcelo-perez')

            if campaiginid == '0035':
                return redirect('/marin-rv-storage')

            if campaiginid == '0036':
                return redirect('/medicare')

            if campaiginid == '0037':
                return redirect('/mob-twenty-two')

            if campaiginid == '0038':
                return redirect('/monster-lead')

            if campaiginid == '0039':
                return redirect('/movement-insurance')

            if campaiginid == '0040':
                return redirect('/naffa-innovations')

            if campaiginid == '0041':
                return redirect('/new-dim-pharmacy')

            if campaiginid == '0042':
                return redirect('/noom')

            if campaiginid == '0043':
                return redirect('/printer-pix')

            if campaiginid == '0044':
                return redirect('/protostar')

            if campaiginid == '0045':
                return redirect('/rainbow-dia-lts')

            if campaiginid == '0046':
                return redirect('/sana-life-science')

            if campaiginid == '0047':
                return redirect('/saura-khalki-fashion')

            if campaiginid == '0048':
                return redirect('/schindler-media')

            if campaiginid == '0049':
                return redirect('/somethings-brewing')

            if campaiginid == '0050':
                return redirect('/sterling-strategies-llc')

            if campaiginid == '0051':
                return redirect('/tanaor-jewelry-lsrael-ltd')

            if campaiginid == '0052':
                return redirect('/tca-counseling-group')

            if campaiginid == '0053':
                return redirect('/tech-report')

            if campaiginid == '0054':
                return redirect('/us-jaclean-inc')

            if campaiginid == '0055':
                return redirect('/ups-nps')

            if campaiginid == '0056':
                return redirect('/window-treatment-unlimited')

            if campaiginid == '0057':
                return redirect('/winopoly')

        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Invalid Password !')
            else:
                messages.info(request, 'Invalid Username and Password !')
            return render(request, 'login.html')

    else:
        logout(request)
        return render(request, 'login.html')

# practo-report
# @login_required
# def practoReport(request):
#     return render(request, 'reports_practo.html')

def logoutNew(request):

    logout(request)
    return render(request, 'login.html')

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
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'settings.html', {'form': form})

# bigo-report
@login_required
def bigoReport(request):
    return render(request, 'reports_bigo.html')

# aadya-reports
@login_required
def AadyaReport(request):
    return render(request, 'reports_aadya.html')

# aditya-birla-cellulose-reports
@login_required
def AdityaBirlaCelluloseReport(request):
    return render(request, 'reports_ab_cellulose.html')

# aditya-birla-toll-free-reports
@login_required
def AdityaBirlaTollFreeReport(request):
    return render(request, 'reports_ab_toll_free.html')

# aditya-birla-nps-reports
@login_required
def AdityaBirlaNPSReport(request):
    return render(request, 'reports_aditya_birla_nps.html')

# aditya-birla-retailer-calling-nps-reports
@login_required
def AdityaBirlaRetailerCallingReport(request):
    return render(request, 'reports_aditya_birla_retailer_calling.html')

# aditya-birla-website-enquiry-reports
@login_required
def AdityaBirlaWebsiteEnquiryReport(request):
    return render(request, 'reports_aditya_birla_website_enquiry.html')

# akdy-calls
@login_required
def AKDYcallsReport(request):
    return render(request, 'reports_akdy.html')

# avenue-living-communities
@login_required
def AvenueLivingCommunitiesReport(request):
    return render(request, 'reports_avenue_living_communities.html')

# bhagyalaxmi-industries
@login_required
def BhagyalaxmiIndustriespractoReport(request):
    return render(request, 'reports_bhagyalaxmi_industries.html')

#bng-vs-php
@login_required
def BNGvsPHP(request):
    return render(request, 'reports_BNG_Vs_PHP.html')

# career-transition-specialist
@login_required
def CareerTransitionSpecialist(request):
    return render(request, 'reports_Career_Transition_Specialist.html')

# citizen-capital
@login_required
def CitizenCapital(request):
    return render(request, 'reports_Citizen_Capital.html')

# core-small-insurance-agency-inc
@login_required
def CoreySmallInsuranceAgencyInc(request):
    return render(request, 'reports_Corey_Small_Insurance_Agency_Inc.html')

# cross-tower
@login_required
def CrossTower(request):
    return render(request, 'reports_Cross_Tower.html')

# csc-service-works
@login_required
def CSCserviceWorks(request):
    return render(request, 'reports_CSC_Service_Works.html')

# daniel-wellington
@login_required
def DanielWellington(request):
    return render(request, 'reports_Daniel_Wellington.html')

# digital-signage
@login_required
def DigitalSignage(request):
    return render(request, 'reports_Digital_Signage.html')

# digital-swiss-gold
@login_required
def DigitalSwissGold(request):
    return render(request, 'reports_Digital_Swiss_Gold.html')

# ee-hh-aaa
@login_required
def EEHHAAA(request):
    return render(request, 'reports_EEHHAAA.html')

# embassy-premium
@login_required
def EmbassyPremium(request):
    return render(request, 'reports_Embassy_Premium.html')

# fame-house
@login_required
def FameHouse(request):
    return render(request, 'reports_Fame_House.html')

# fitness-mortgage
@login_required
def FitnessMortgage(request):
    return render(request, 'reports_Finesse_Mortgage.html')


# genesis-acquisition
@login_required
def GenesisAccquisition(request):
    return render(request, 'reports_Genesis_Acquisition.html')

# golden-eye-cctv
@login_required
def GoldenEyeCCTV(request):
    return render(request, 'reports_Golden_Eye_CCTV.html')

# gubagoo
@login_required
def Gubagoo(request):
    return render(request, 'reports_Gubagoo.html')

# hindalco
@login_required
def Hindalco(request):
    return render(request, 'reports_Hindalco.html')

# ilm
@login_required
def ILM(request):
    return render(request, 'reports_ILM.html')

# imaginarium
@login_required
def ImaginariumSolutionsLTD(request):
    return render(request, 'reports_Imaginarium_Solutions_Ltd.html')

# imprint-plus
@login_required
def ImprintPlus(request):
    return render(request, 'reports_Imprint_Plus.html')

# insalvage
@login_required
def Insalvage(request):
    return render(request, 'reports_Insalvage.html')

# kaapi-machines
@login_required
def KaapiMachines(request):
    return render(request, 'reports_Kaapi_Machines.html')

# lawoffice-m-geller
@login_required
def LawOfficesRobertMgeller(request):
    return render(request, 'reports_LAW_OFFICES_OF_ROBERT_M._GELLER.html')


# marcelo-perez
@login_required
def MarceloPerezStateFarm(request):
    return render(request, 'reports_MARCELO_PEREZ_STATE_FARM.html')

# marin-rv-storage
@login_required
def MarinRVstorage(request):
    return render(request, 'reports_Marin_RV_Storage.html')

# medicare
@login_required
def MediCare(request):
    return render(request, 'reports_Medicare.html')

# mob-twenty-two
@login_required
def MobileTwentyTwo(request):
    return render(request, 'reports_Mobile_22.html')

# monster-lead
@login_required
def MonsterLead(request):
    return render(request, 'reports_Monster_Lead.html')

# movement-insurance
@login_required
def MovementInsurance(request):
    return render(request, 'reports_Movement_Insurance.html')

# naffa-innovations
@login_required
def NaffaInnovations(request):
    return render(request, 'reports_Naffa_Innovations.html')

# new-dim-pharmacy
@login_required
def NewDimensionPharmacy(request):
    return render(request, 'reports_New_Dimension_Pharmacy.html')

# noom
@login_required
def Noom(request):
    return render(request, 'reports_Noom.html')

# printer-pix
@login_required
def PrinterPix(request):
    return render(request, 'reports_Printerpix.html')

# protostar
@login_required
def Protostar(request):
    return render(request, 'reports_Protostar.html')

# rainbow-dia-lts
@login_required
def RainbowDiagnosticsLTS(request):
    return render(request, 'reports_RainBow_Diagnostics_LTS.html')

# sana-life-science
@login_required
def SanaLifeScience(request):
    return render(request, 'reports_Sana_Life_Science.html')

# saura-khalki-fashion
@login_required
def SaurabhaktiKhalkiFasion(request):
    return render(request, 'reports_Saurabhakti_Khalki_Fashion.html')

# schindler-media
@login_required
def SchindlerMedia(request):
    return render(request, 'reports_Schindler_Media.html')

# somethings-brewing
@login_required
def SomethingsBrewing(request):
    return render(request, "reports_Something's_Brewing.html")


# sterling-strategies-llc
@login_required
def SterlingStrategiesLLC(request):
    return render(request, 'reports_Sterling_Strategies_Llc.html')


# tanaor-jewelry-lsrael-ltd
@login_required
def TanaorJewelryIsraelLtd(request):
    return render(request, 'reports_Tanaor_Jewelry_Israel_Ltd.html')

# tca-counseling-group
@login_required
def TCAcounselingGroup(request):
    return render(request, 'reports_TCA_Counseling_Group.html')


# tech-report
@login_required
def TechReport(request):
    return render(request, 'reports_Tech_Report.html')

# us-jaclean-inc
@login_required
def USJacleanINC(request):
    return render(request, 'reports_U_S_JACLEAN_INC.html')

# ups-nps
@login_required
def UPSNPS(request):
    return render(request, 'reports_UPS_NPS.html')

# window-treatment-unlimited
@login_required
def WindowTreatmentUnlimited(request):
    return render(request, 'reports_Window_Treatment_Unlimited.html')

# winopoly
@login_required
def Winopoly(request):
    return render(request, 'reports_Winopoly.html')


