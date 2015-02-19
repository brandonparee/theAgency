from django.db import models

<<<<<<< HEAD
class Beer(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 75)
	birth = models.DateField()
	zipcode = models.CharField(max_length = 5)
=======
class CampaignBeer(models.Model):
	name=models.CharField(max_length = 200)
	email=models.EmailField(max_length = 75)
	birth=models.CharField(max_length=5)
>>>>>>> 13e177590743abbf8805e8c1d942477cf7e1b2db
