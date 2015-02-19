from django.db import models
from django.core.validators import RegexValidator

class Shirt(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 75)
    SHIRT_SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    shirt_size = models.CharField(max_length = 3, choices = SHIRT_SIZE_CHOICES, default = "M")
    COLOR_CHOICES = (
        ('W', 'White'),
        ('G', 'Gray'),
        ('B', 'Black')
    )
    color = models.CharField(max_length = 1, choices = COLOR_CHOICES, default = "White")
    CUT_CHOICES = (
        ('M', 'Unisex'),
        ("F", 'Womens')
    )
    cut = models.CharField(max_length = 1, choices = CUT_CHOICES, default = "Unisex")
    zipcode_validatior = RegexValidator(regex = '^\d{5}(?:[-\s]\d{4})?$')
    zipcode = models.CharField(validators = [zipcode_validatior], max_length = 5)