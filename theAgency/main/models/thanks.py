from django.db import models

class Thanks(models.Model):
	message = models.CharField(max_length = 200)
	url = models.CharField(max_length = 75)