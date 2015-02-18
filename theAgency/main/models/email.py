from django.db import models

class CaptureEmail(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 75)