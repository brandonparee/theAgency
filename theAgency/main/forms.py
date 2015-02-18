from django import forms
from main.models import Compaign
#from django.forms import ModelForm

class CompaignForm(forms.ModelForm):
	class Meta:
		model = Compaign
		fields = ['name', 'description', 'founddate', 'image']