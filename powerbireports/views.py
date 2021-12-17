from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .models import *


# Create your views here.
# login-page
def loginPage(request):
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
                return redirect('/all')

            # this is for other reports login
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

            if campaiginid == '0058':
                return redirect('/practo')

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
    return render(request, 'settings.html', {'form': form})


# bigo-report
@login_required
def bigoReport(request):
    if request.user.profile.campaignid == '0001' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_bigo.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# aadya-reports
@login_required
def aadyaReport(request):
    if request.user.profile.campaignid == '0002' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aadya.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# aditya-birla-cellulose-reports
@login_required
def adityaBirlaCelluloseReport(request):
    if request.user.profile.campaignid == '0003' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_ab_cellulose.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# aditya-birla-toll-free-reports
@login_required
def adityaBirlaTollFreeReport(request):
    if request.user.profile.campaignid == '0004' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_ab_toll_free.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# aditya-birla-nps-reports
@login_required
def adityaBirlaNPSReport(request):
    if request.user.profile.campaignid == '0005' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aditya_birla_nps.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# aditya-birla-retailer-calling-nps-reports
@login_required
def adityaBirlaRetailerCallingReport(request):
    if request.user.profile.campaignid == '0006' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aditya_birla_retailer_calling.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# aditya-birla-website-enquiry-reports
@login_required
def adityaBirlaWebsiteEnquiryReport(request):
    if request.user.profile.campaignid == '0007' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_aditya_birla_website_enquiry.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# akdy-calls
@login_required
def aKDYcallsReport(request):
    if request.user.profile.campaignid == '0008' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_akdy.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# avenue-living-communities
@login_required
def avenueLivingCommunitiesReport(request):
    if request.user.profile.campaignid == '0009' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_avenue_living_communities.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# bhagyalaxmi-industries
@login_required
def bhagyalaxmiIndustriespractoReport(request):
    if request.user.profile.campaignid == '0010' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_bhagyalaxmi_industries.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# bng-vs-php
@login_required
def bNGvsPHPreport(request):
    if request.user.profile.campaignid == '0011' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_BNG_Vs_PHP.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# career-transition-specialist
@login_required
def careerTransitionSpecialistReport(request):
    if request.user.profile.campaignid == '0012' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Career_Transition_Specialist.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# citizen-capital
@login_required
def citizenCapitalReport(request):
    if request.user.profile.campaignid == '0013' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Citizen_Capital.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# core-small-insurance-agency-inc
@login_required
def coreySmallInsuranceAgencyIncReport(request):
    if request.user.profile.campaignid == '0014' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Corey_Small_Insurance_Agency_Inc.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# cross-tower
@login_required
def crossTowerReport(request):
    if request.user.profile.campaignid == '0015' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Cross_Tower.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# csc-service-works
@login_required
def cSCserviceWorksReport(request):
    if request.user.profile.campaignid == '0016' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_CSC_Service_Works.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# daniel-wellington
@login_required
def danielWellingtonReport(request):
    if request.user.profile.campaignid == '0017' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Daniel_Wellington.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# digital-signage
@login_required
def digitalSignageReport(request):
    if request.user.profile.campaignid == '0018' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Digital_Signage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# digital-swiss-gold
@login_required
def digitalSwissGoldReport(request):
    if request.user.profile.campaignid == '0019' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Digital_Swiss_Gold.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# ee-hh-aaa
@login_required
def eEHHAAAreport(request):
    if request.user.profile.campaignid == '0020' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_EEHHAAA.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# embassy-premium
@login_required
def embassyPremiumReport(request):
    if request.user.profile.campaignid == '0021' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Embassy_Premium.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# fame-house
@login_required
def fameHouseReport(request):
    if request.user.profile.campaignid == '0022' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Fame_House.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# fitness-mortgage
@login_required
def fitnessMortgageReport(request):
    if request.user.profile.campaignid == '0023' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Finesse_Mortgage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# genesis-acquisition
@login_required
def genesisAccquisitionReport(request):
    if request.user.profile.campaignid == '0024' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Genesis_Acquisition.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# golden-eye-cctv
@login_required
def goldenEyeCCTVreport(request):
    if request.user.profile.campaignid == '0025' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Golden_Eye_CCTV.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# gubagoo
@login_required
def gUbagooReport(request):
    if request.user.profile.campaignid == '0026' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Gubagoo.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# hindalco
@login_required
def hindalcoReport(request):
    if request.user.profile.campaignid == '0027' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Hindalco.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# ilm
@login_required
def iLMreport(request):
    if request.user.profile.campaignid == '0028' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_ILM.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# imaginarium
@login_required
def imaginariumSolutionsLTDreport(request):
    if request.user.profile.campaignid == '0029' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Imaginarium_Solutions_Ltd.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# imprint-plus
@login_required
def imprintPlusReport(request):
    if request.user.profile.campaignid == '0030' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Imprint_Plus.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# insalvage
@login_required
def iNsalvageReport(request):
    if request.user.profile.campaignid == '0031' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Insalvage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# kaapi-machines
@login_required
def kaapiMachinesReport(request):
    if request.user.profile.campaignid == '0032' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Kaapi_Machines.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# lawoffice-m-geller
@login_required
def lawOfficesRobertMgellerReport(request):
    if request.user.profile.campaignid == '0033' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_LAW_OFFICES_OF_ROBERT_M._GELLER.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# marcelo-perez
@login_required
def marceloPerezStateFarmReport(request):
    if request.user.profile.campaignid == '0034' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_MARCELO_PEREZ_STATE_FARM.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# marin-rv-storage
@login_required
def marinRVstorageReport(request):
    if request.user.profile.campaignid == '0035' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Marin_RV_Storage.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# medicare
@login_required
def mediCareReport(request):
    if request.user.profile.campaignid == '0036' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Medicare.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# mob-twenty-two
@login_required
def mobileTwentyTwoReport(request):
    if request.user.profile.campaignid == '0037' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Mobile_22.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# monster-lead
@login_required
def monsterLeadReport(request):
    if request.user.profile.campaignid == '0038' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Monster_Lead.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# movement-insurance
@login_required
def movementInsuranceReport(request):
    if request.user.profile.campaignid == '0039' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Movement_Insurance.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# naffa-innovations
@login_required
def naffaInnovationsReport(request):
    if request.user.profile.campaignid == '0040' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Naffa_Innovations.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# new-dim-pharmacy
@login_required
def newDimensionPharmacyReport(request):
    if request.user.profile.campaignid == '0041' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_New_Dimension_Pharmacy.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# noom
@login_required
def noomReport(request):
    if request.user.profile.campaignid == '0042' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Noom.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# printer-pix
@login_required
def printerPixReport(request):
    if request.user.profile.campaignid == '0043' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Printerpix.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# protostar
@login_required
def protostarReport(request):
    if request.user.profile.campaignid == '0044' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Protostar.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# rainbow-dia-lts
@login_required
def rainbowDiagnosticsLTSreport(request):
    if request.user.profile.campaignid == '0045' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_RainBow_Diagnostics_LTS.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# sana-life-science
@login_required
def sanaLifeScienceReport(request):
    if request.user.profile.campaignid == '0046' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Sana_Life_Science.html')
    else:

        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# saura-khalki-fashion
@login_required
def saurabhaktiKhalkiFasionReport(request):
    if request.user.profile.campaignid == '0047' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Saurabhakti_Khalki_Fashion.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# schindler-media
@login_required
def schindlerMediaReport(request):
    if request.user.profile.campaignid == '0048' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Schindler_Media.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# somethings-brewing
@login_required
def somethingsBrewingReport(request):
    if request.user.profile.campaignid == '0049' or request.user.profile.campaignid == 'all':
        return render(request, "reports_Something's_Brewing.html")
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# sterling-strategies-llc
@login_required
def sterlingStrategiesLLCreport(request):
    if request.user.profile.campaignid == '0050' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Sterling_Strategies_Llc.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# tanaor-jewelry-lsrael-ltd
@login_required
def tanaorJewelryIsraelLtdReport(request):
    if request.user.profile.campaignid == '0051' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Tanaor_Jewelry_Israel_Ltd.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# tca-counseling-group
@login_required
def tCAcounselingGroupReport(request):
    if request.user.profile.campaignid == '0052' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_TCA_Counseling_Group.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# tech-report
@login_required
def techReport(request):
    if request.user.profile.campaignid == '0053' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Tech_Report.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# us-jaclean-inc
@login_required
def uSJacleanINCreport(request):
    if request.user.profile.campaignid == '0054' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_U_S_JACLEAN_INC.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# ups-nps
@login_required
def uPSNPSreport(request):
    if request.user.profile.campaignid == '0055' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_UPS_NPS.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# window-treatment-unlimited
@login_required
def windowTreatmentUnlimitedReport(request):
    if request.user.profile.campaignid == '0056' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Window_Treatment_Unlimited.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# winopoly
@login_required
def winopolyReport(request):
    if request.user.profile.campaignid == '0057' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Winopoly.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# Practo
@login_required
def PractoReport(request):
    if request.user.profile.campaignid == '0058' or request.user.profile.campaignid == 'all':
        return render(request, 'reports_Practo_Technologies_Cumulative.html')
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


# all
@login_required
def managementDashboard(request):
    if request.user.profile.campaignid == 'all':
        pro = Profile.objects.exclude(campaignid="all")
        data = {'profile': pro}
        return render(request, 'reports_all.html', data)
    else:
        messages.info(request, "You were logged out due to unauthorized access.")
        return redirect('/logout')


@login_required
def mgtReport(request, cid):
    campaiginid = cid

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

    if campaiginid == '0058':
        return redirect('/practo')
