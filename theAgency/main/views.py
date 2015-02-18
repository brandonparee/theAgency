from django.shortcuts import render
#from django import ModelForm
from django.http import HttpResponse
#from django.http import 
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Compaign

#from django.views.decorators.csrf import ensure_csrf_cookie
#@ensure_csrf_cookie

def home(request):
	return render(request, 'main/index.html', {})

def form(request):
	CampaignFormSet = modelformset_factory(Compaign)
	if request.method == 'POST':
		formset = CampaignFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
			#do something.
	else:
		formset = CampaignFormSet()
	return render_to_response("main/form.html", {"formset": formset,}, context_instance=RequestContext(request))	

#if form.is_valid():
#	mi= MoreInfo()
#	mi.email = form.cleaned_data["email"]
#	mi.name = form.cleaned_data["name"]
#	mi.save()
#	return HttpResponseRedirect("/thanks/")
#elif request.method == 'GET':
#	form - MoreInfoForm()
#else:
#	return HttpResponseRedirect("/404/")
#return render(request, 'main/form.html' {"form": form})