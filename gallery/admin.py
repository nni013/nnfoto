from django.contrib import admin
from gallery.models import Album, Picture

class PictureInline(admin.TabularInline):
	model = Picture
	extra = 1

class AlbumAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['album_name']}),
		('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [PictureInline]

	list_display = ('album_name', 'pub_date', 'was_published_recently')
#Album.objects.get().picture_set.count(),
admin.site.register(Album, AlbumAdmin)
