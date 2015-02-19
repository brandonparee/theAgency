from django.db import models

class Giveaway(models.Model):
	quantity = models.CharField(max_length=200)
	item = models.CharField(max_length=200)
	image = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	campaign_fk = models.ForeignKey('Campaign')