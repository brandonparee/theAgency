from django import forms
from main.models import Personal, CaptureEmail
#from django.forms import ModelForm

class PersonalForm(forms.ModelForm):
	class Meta:
		model = Personal
		fields = ['name', 'email', 'birth', 'gender', 'zipcode']

class EmailForm(forms.ModelForm):
	class Meta:
		model = CaptureEmail
		fields = ['name', 'email']