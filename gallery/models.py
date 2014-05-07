from django.db import models

class Album(models.Model):
	album_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')

class Picture(models.Model):
	pic_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')