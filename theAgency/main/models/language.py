from django.db import models

class Language(models.Model):
	name=models.CharField(max_length = 200)
	email=models.EmailField(max_length = 75)
	birth=models.CharField(min_length=5, max_length=5)