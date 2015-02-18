from django.shortcuts import render#, redirect
from django.http import HttpResponseRedirect
#from django.template import RequestContext
#from django.forms import ModelForm
#from main.models import Compaign
from main.forms import CompaignForm

def home(request):
	return render(request, 'main/index.html', {})

def form(request):
  if request.method == 'POST':
    form = CompaignForm(request.POST)
    if form.is_valid():
    	form.save()
    	return HttpResponseRedirect('/worked yay/')
  else:
    form = CompaignForm()
  return render(request, 'main/form.html', {'form': form})