from django import forms
<<<<<<< HEAD
from main.models import Email, Beer, Language, Shirt

class EmailForm(forms.ModelForm):
	class Meta:
		model = Email
		fields = ['name', 'email']

class BeerForm(forms.ModelForm):
	class Meta:
		model = Beer
		fields = ['name', 'email', 'birth', 'zipcode']

class LanguageForm(forms.ModelForm):
	class Meta:
		model = Language
		fields = ['email']

class ShirtForm(forms.ModelForm):
	class Meta:
		model = Shirt
		fields = ['name', 'email', 'shirt_size', 'color', 'cut', 'zipcode']
=======
from main.models import CampaignEmail
#from django.forms import ModelForm

class EmailForm(forms.ModelForm):
	class Meta:
		model = CampaignEmail
		fields = ['name', 'email']
>>>>>>> 13e177590743abbf8805e8c1d942477cf7e1b2db
