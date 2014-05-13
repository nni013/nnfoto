import datetime
import os
from django.db import models
from django.utils import timezone


class Album(models.Model):
	album_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')

	def __unicode__(self):
		return self.album_name

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

def file_path(instance, filename):
	return '/'.join(['gallery', str(instance.album.id), filename])

class Picture(models.Model):
	album = models.ForeignKey(Album)
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')
#	path = 
	imgfile = models.ImageField(upload_to=file_path)

	def __unicode__(self):
		return self.name

	def delete(self, *args, **kwargs):
		self.imgfile.delete(False)
		super(Picture, self).delete(*args, **kwargs)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

