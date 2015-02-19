from django.db import models

class CampaignEmail(models.Model):
	campaign_name = models.CharField(max_length=200)
	description = models.TextField(max_length=2000)
	image = models.CharField(max_length=200)
	background = models.CharField(max_length=200)

	def __str__(self):
		return self.name