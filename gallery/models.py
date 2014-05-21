import datetime
import os
import shutil
from django.db import models
from django.utils import timezone


class Album(models.Model):
	album_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published', auto_now_add=True)

	def __unicode__(self):
		return self.album_name

	def delete(self, *args, **kwargs):
		shutil.rmtree('media/gallery/'+str(self.id)+'/')
		super(Album, self).delete(*args, **kwargs)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

def file_path(instance, filename):
	return '/'.join(['gallery', str(instance.album.id), filename])

def thumb_path(instance, filename):
	return '/'.join(['gallery', str(instance.album.id), 'thumbs', filename])

class Picture(models.Model):
	album = models.ForeignKey(Album)
	name = models.CharField(max_length=200, blank=True)
	pub_date = models.DateTimeField('Date published', auto_now_add=True)
#	path = 
	imgfile = models.ImageField(upload_to=file_path)
	thumbnail = models.ImageField(upload_to=thumb_path, blank=True, null=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.name == "":
			self.name = os.path.basename(self.imgfile.name)
		self.make_thumbnail()
		super(Picture, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		self.imgfile.delete(False)
		super(Picture, self).delete(*args, **kwargs)

	def make_thumbnail(self):
		if not self.imgfile:
			return

		from PIL import Image
		from cStringIO import StringIO
		from django.core.files.uploadedfile import SimpleUploadedFile

		THUMBNAIL_SIZE = (200, 200)

		DJANGO_TYPE = self.imgfile.file.content_type

		if DJANGO_TYPE == 'image/jpeg':
			PIL_TYPE = 'jpeg'
			FILE_EXTENSION = 'jpg'
		elif DJANGO_TYPE == 'image/png':
			PIL_TYPE = 'png'
			FILE_EXTENSION = 'png'

		img = Image.open(StringIO(self.imgfile.read()))

		img.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

		temp_handle = StringIO()
		img.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		suf = SimpleUploadedFile(os.path.split(self.imgfile.name)[-1],
			temp_handle.read(), content_type=DJANGO_TYPE)

		self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0], FILE_EXTENSION), suf, save=False)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

