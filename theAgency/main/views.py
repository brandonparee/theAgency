from django.shortcuts import render#, redirect
from django.http import HttpResponseRedirect
#from django.template import RequestContext
#from django.forms import ModelForm
#from main.models import Compaign
from main.forms import CompaignForm, AccountForm, GiveawayForm

def home(request):
	return render(request, 'main/index.html', {})

def makeAgency(request):
  if request.method == 'POST':
    form = CompaignForm(request.POST)
    if form.is_valid():
    	form.save()
    	return HttpResponseRedirect('/worked yay/')
  else:
    form = CompaignForm()
  return render(request, 'main/makeAgency.html', {'form': form})

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