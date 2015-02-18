from django.db import models

class Compaign(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=2000)
	founddate = models.DateField()
	image = models.CharField(max_length=200)

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

#how to see whats in the database through CMD:
#CMD: python manage.py dumpdata <appname> <options>
#	python manage.py dumpdata database --indent 2
#
#how to clear data from tables
#CMD: python manage.py flush
#
#how to load data into tables provided by the fixtures file (the default data that should belong in the database)
#CMD: python manage.py loaddata database_data.json
#
#What to edit what populates the tables when performing loaddata
#edit the fixtures file located at .\theTheatre\theTheatre\database\fixtures\database_test.json
#
#
#ask about this first before messing with:
#migrations are used to switch between different setups for the tables
#this includes things like renaming, adding, removing rows and changing the conditions for data, etc
#
#how to make a new migration (each migration is listed by a number 'xxxx')
#migations are useful for editing the model
#
#CMD: python manage.py makemigration <appname>
#	python manage.py makemigrations database
#
#how to migrate to a migration('xxxx' is the migration number)
#
#CMD: python manage.py sqlmigrate <appname> xxxx
#	python manage.py sqlmigrate database 0002
#
#CMD: python manage.py migrate