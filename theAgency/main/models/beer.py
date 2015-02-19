from django.db import models

class Beer(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 75)
	birth = models.DateField()
	zipcode = models.CharField(max_length = 5)