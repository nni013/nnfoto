from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nnfoto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/', include('gallery.urls')),
) + static(settings.MEDIA_URL, image_root=settings.MEDIA_ROOT)
