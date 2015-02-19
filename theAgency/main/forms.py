from django import forms
from main.models import CampaignEmail
#from django.forms import ModelForm

class EmailForm(forms.ModelForm):
	class Meta:
		model = CampaignEmail
		fields = ['name', 'email']