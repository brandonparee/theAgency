from django import forms
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
		fields = ['name', 'email', 'language', 'race', 'birth', 'zipcode']

class ShirtForm(forms.ModelForm):
	class Meta:
		model = Shirt
		fields = ['name', 'email', 'shirt_size', 'color', 'cut', 'zipcode']