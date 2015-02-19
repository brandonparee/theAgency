from django.db import models

class CampaignEmail(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 75)