import datetime
import os
from django.db import models
from django.utils import timezone


class Album(models.Model):
	album_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')
#	os.mkdir(os.path.join('/gallery/media/images', models.ForeignKey(Album)))

	def __unicode__(self):
		return self.album_name

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Picture(models.Model):
	album = models.ForeignKey(Album)
	pic_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')
#	pic_loc = models.FileField(upload_to='/media/images/'+str(album))

	def __unicode__(self):
		return self.pic_name

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
