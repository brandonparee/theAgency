from django import forms
from main.models import Campaign, Account, Giveaway, CaptureEmail
#from django.forms import ModelForm

class CampaignForm(forms.ModelForm):
	class Meta:
		model = Campaign
		fields = ['name', 'description', 'image']

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['name', 'email', 'birth', 'gender', 'campaign_fk', 'questions', 'comments']

class GiveawayForm(forms.ModelForm):
	class Meta:
		model = Giveaway
		fields = ['quantity', 'item', 'image', 'description', 'campaign_fk']

class EmailForm(forms.ModelForm):
	class Meta:
		model = CaptureEmail
		fields = ['name', 'email']