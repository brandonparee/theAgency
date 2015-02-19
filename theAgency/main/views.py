from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.template import RequestContext
from main.models import CampaignEmail
from main.forms import EmailForm

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
  emails = {'Emails': CampaignEmail.objects.all()}
  return render(request, 'main/all_emails.html', emails)