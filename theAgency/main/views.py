from django.shortcuts import render#, redirect
from django.http import HttpResponseRedirect
#from django.template import RequestContext
#from django.forms import ModelForm
from main.models import Campaign, Giveaway
from main.forms import CampaignForm, AccountForm, GiveawayForm

def home(request):
	return render(request, 'main/index.html', {})

def makeCampaign(request):
  if request.method == 'POST':
    form = CampaignForm(request.POST)
    if form.is_valid():
    	form.save()
    	return HttpResponseRedirect('/worked yay/')
  else:
    form = CampaignForm()
  return render(request, 'main/makeCampaign.html', {'form': form})

def makeAccount(request):
  if request.method == 'POST':
    form = AccountForm(request.POST)
    if form.is_valid():
    	form.save()
    	return HttpResponseRedirect('/worked yay/')
  else:
    form = AccountForm()
  return render(request, 'main/makeAccount.html', {'form': form})


def makeGiveaway(request):
	if request.method == 'POST':
		form = GiveawayForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/worked yay/')
	else:
		form = GiveawayForm()
	return render(request, 'main/makeGiveaway.html', {'form': form})

def campaign(request, id_num):
  try:
    campaigns = Campaign.objects.get(id=id_num)
  except Campaign.DoesNotExist:
    return HttpResponseRedirect('/campaigns/')
  try:
    giveaways = Giveaway.objects.get(campaign_fk=id_num)
  except Giveaway.DoesNotExist:
    giveaways = None
  return render(request, 'main/campaign.html', {'Campaign': Campaign.objects.get(id=id_num), 'Giveaways': giveaways})

def campaigns(request):
  return render(request, 'main/campaigns.html', {'Campaigns': Campaign.objects.all()})