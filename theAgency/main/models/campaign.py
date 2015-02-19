from django.db import models

class Campaign(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=2000)
	image = models.CharField(max_length=200)

	def __str__(self):
		return self.name