from django.db import models

class CampaignShirt(models.Model):
    name=models.CharField(max_length = 200)
    email=models.EmailField(max_length = 75)
    SHIRT_SIZE_CHOICES=(
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('Other', 'Other')
    )
    shirt_size=models.CharField(max_length=5, choices=SHIRT_SIZE_CHOICES, default="Other")
    COLOR_CHOICES = (
        ('White', 'W'),
        ('Gray', 'G'),
        ('Black', 'B')
    )
    color=models.CharField(max_length=5, choices=COLOR_CHOICES, default="White")
    CUT_CHOICES = (
        ('Unisex', 'M'),
        ("Women", 'F')
    )
    cut=models.CharField(max_length=1, choices=CUT_CHOICES, default="Unisex")
    zipcode=models.CharField(max_length=5)