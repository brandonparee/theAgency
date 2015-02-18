from django.db import models

class Compaign(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=2000)
	founder = models.CharField(max_length=50)
	founddate = models.DateField()
	image = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Account(models.Model):
	name = models.CharField(max_length=50)
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Secret', 'Secret'),
		('Both', 'Both'),
		('Alpha', 'Alpha Male'),
		('Dog', 'My gender is: Dog'),
		('Cow', 'Cow because cows are the best.'),
	)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Secret')
	email = models.EmailField(max_length=75)
	birth = models.DateField()
	questions = models.TextField(max_length=2000)
	comments = models.TextField(max_length=2000)
	compaign_fk = models.ForeignKey('Compaign')

class Giveaway(models.Model):
	quantity = models.CharField(max_length=200)
	item = models.CharField(max_length=200)
	image = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	compaign_fk = models.ForeignKey('Compaign')