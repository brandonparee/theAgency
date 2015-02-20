from django import forms
from main.models import Email, Beer, Language, Shirt

date_widget =  {
            'birth': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }

class EmailForm(forms.ModelForm):
	class Meta:
		model = Email
		fields = ['name', 'email']

class BeerForm(forms.ModelForm):
	class Meta:
		model = Beer
		widgets = date_widget
		fields = ['name', 'email', 'birth', 'zipcode']

class LanguageForm(forms.ModelForm):
	class Meta:
		model = Language
		widgets = date_widget
		fields = ['name', 'email', 'language', 'race', 'birth', 'zipcode']

class ShirtForm(forms.ModelForm):
	class Meta:
		model = Shirt
		widgets = date_widget
		fields = ['name', 'email', 'shirt_size', 'color', 'cut', 'zipcode']