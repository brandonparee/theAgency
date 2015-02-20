from django.db import models
from django.core.validators import RegexValidator

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
        ('Other', 'Other')
    )
    language = models.CharField(max_length = 10, choices = LANGUAGE_CHOICES, default = "English")
    RACE_CHOICES = (
        ('Caucasian', 'Caucasian'),
        ('African American', 'African American'),
        ('Hispanic', 'Hispanic'),
        ('Asian', 'Asian'),
        ('Middle Eastern', 'Middle Eastern'),
        ('Pacific Islander', 'Pacific Islander'),
        ('Native American', 'Native American'),
        ('Other', 'Other')
    )
    race = models.CharField(max_length = 16, choices = RACE_CHOICES, default = "Caucasian")
    birth = models.DateField()
    zipcode_validatior = RegexValidator(regex = '^\d{5}(?:[-\s]\d{4})?$')
    zipcode = models.CharField(validators = [zipcode_validatior],max_length = 5)
