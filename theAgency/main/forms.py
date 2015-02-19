from django import forms
from main.models import Campaign, Personal, Giveaway, CaptureEmail
#from django.forms import ModelForm

class CampaignForm(forms.ModelForm):
	class Meta:
		model = Campaign
		fields = ['name', 'description', 'image']

class PersonalForm(forms.ModelForm):
	class Meta:
		model = Personal
		fields = ['name', 'email', 'birth', 'gender', 'zipcode', 'campaign_fk']

class GiveawayForm(forms.ModelForm):
	class Meta:
		model = Giveaway
		fields = ['quantity', 'item', 'image', 'description', 'campaign_fk']

class EmailForm(forms.ModelForm):
	class Meta:
		model = CaptureEmail
		fields = ['name', 'email']