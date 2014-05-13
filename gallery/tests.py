import datetime

from django.test import TestCase
from django.utils import timezone

from gallery.models import Album, Picture

class AlbumModelTests(TestCase):

	def test_was_published_recently_with_future_album(self):
		"""
		was_published_recently() should return False for albums whose
		pub_date is in the future.
		"""
		future_album = Album(album_name="Future album", pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_album.was_published_recently(), False)

	def test_was_published_recently_with_old_album(self):
		"""
		was_published_recently() should return False for albums whose pub_date
		is older than 1 day.
		"""
		old_album = Album(album_name="Old album", pub_date=timezone.now() - datetime.timedelta(days=2))
		self.assertEqual(old_album.was_published_recently(), False)

	def test_was_published_recently_with_recent_album(self):
		"""
		was_published_recently() should return True for albums whose pub_date
		is within the last day.
		"""
		recent_album = Album(album_name="Recent album", pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_album.was_published_recently(), True)

class PictureModelTests(TestCase):

	def test_was_published_recently_with_future_picture(self):
		"""
		was_published_recently() should return False for pictures whose
		pub_date is in the future.
		"""
		future_pic = Picture(name="Future picture", pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_pic.was_published_recently(), False)

	def test_was_published_recently_with_old_picture(self):
		"""
		was_published_recently() should return False for pictures whose pub_date
		is older than 1 day.
		"""
		old_pic = Picture(name="Old picture", pub_date=timezone.now() - datetime.timedelta(days=2))
		self.assertEqual(old_pic.was_published_recently(), False)

	def test_was_published_recently_with_recent_picture(self):
		"""
		was_published_recently() should return True for pictures whose pub_date
		is within the last day.
		"""
		recent_pic = Picture(name="Recent picture", pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_pic.was_published_recently(), True)
