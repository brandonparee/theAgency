from django.db import models

class Language(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 75)
    LANGUAGE_CHOICES = (
        ('English', 'English'),
        ('Mandarin', 'Mandarin'),
        ('Spanish', 'Spanish'),
        ('Hindi', 'Hindi'),
        ('Arabic', 'Arabic'),
        ('Portuguese', 'Portuguese'),
        ('Bengali', 'Bengali'),
        ('Russian', 'Russian'),
        ('Japanese', 'Japanese'),
        ('Punjabi', 'Punjabi'),
    )
    language = models.CharField(max_length = 10, choices = COLOR_CHOICES, default = "English")
    RACE_CHOICES = (
        ('Caucasian', 'Caucasian'),
        ('African American', 'African American'),
        ('Hispanic', 'Hispanic'),
        ('Asian', 'Asian'),
        ('Middle Eastern', 'Middle Eastern'),
        ('Pacific Islander', 'Pacific Islander'),
        ('Native American', 'Native American'),
        ('Other', 'Other'),
        ('Japanese', 'Japanese'),
        ('Punjabi', 'Punjabi'),
    )
    race = models.CharField(max_length = 16, choices = COLOR_CHOICES, default = "English")
	birth = models.DateField()
    zipcode = models.EmailField(max_length = 5)
