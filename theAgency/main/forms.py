from django import forms
from main.models import Compaign, Account, Giveaway
#from django.forms import ModelForm

class CompaignForm(forms.ModelForm):
	class Meta:
		model = Compaign
		fields = ['name', 'description', 'founder', 'founddate', 'image']

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['name', 'email', 'birth', 'gender', 'compaign_fk', 'questions', 'comments']

class GiveawayForm(forms.ModelForm):
	class Meta:
		model = Giveaway
		fields = ['quantity', 'item', 'image', 'description', 'compaign_fk']