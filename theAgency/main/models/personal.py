from django.db import models

class Personal(models.Model):
	name = models.CharField(max_length=50)
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Secret', 'Secret'),
	)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Secret')
	SHIRT_SIZE_CHOICES = (
		('XS', 'XS'),
		('S', 'S'),
		('M', 'M'),
		('L', 'L'),
		('XL', 'XL'),
		('XXL', 'XXL'),
		('Other', 'Other')
	)
	shirt_size = models.CharField(max_length=3, choices=SHIRT_SIZE_CHOICES, default="Other")
	RACE_CHOICES = (
		('Caucasian', 'Caucasian'),
		('Hispanic', 'Hispanic'),
		('Asian', 'Asian'),
		('African American', 'African American'),
		('Other', 'Other'),
		)
	race = models.CharField(max_length=3, choices=RACE_CHOICES, default="Other")
	email = models.EmailField(max_length=75)
	birth = models.DateField()
	zipcode = models.IntegerField(max_length=5)