from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.template import RequestContext
from main.models import CaptureEmail, Personal, CampaignEmail
from main.forms import EmailForm, PersonalForm

def home(request):
	return render(request, 'main/index.html', {})

def EmailCapture(request):
  if request.method == 'POST':
    form = EmailForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/emails/')
  else:
    form = EmailForm()
  return render(request, 'main/email_capture.html', {'form': form})

def AllEmails(request):
  emails = {'Emails': CaptureEmail.objects.all()}
  return render(request, 'main/all_emails.html', emails)

def campaign(request, id_num):
  try:
    giveaways = Giveaway.objects.get(campaign_fk=id_num)
  except Giveaway.DoesNotExist:
    giveaways = None
  return render(request, 'main/campaign.html', {'campaign': Campaign.objects.get(id=id_num), 'giveaways': giveaways})

def campaigns(request):
  return render(request, 'main/campaigns.html', {'campaigns': Campaign.objects.all()})