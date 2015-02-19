from django.db import models

class Personal(models.Model):
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
	campaign_fk = models.ForeignKey('Campaign')