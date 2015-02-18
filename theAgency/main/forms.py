from django import forms
from main.models import Compaign, Account, Giveaway
#from django.forms import ModelForm

class CompaignForm(forms.ModelForm):
	class Meta:
		model = Compaign
		fields = ['name', 'description', 'founddate', 'image']

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['name', 'gender', 'email', 'birth', 'compaign_fk']

class GiveawayForm(forms.ModelForm):
	class Meta:
		model = Giveaway
		fields = ['quantity', 'item', 'image', 'description', 'compaign_fk']