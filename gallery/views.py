from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
#from .forms import UploadFileForm
from .models import Picture

# Create your views here.
def index(request):
	template = loader.get_template('gallery/upload.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))


"""
def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			instance = Picture(file = request.FILES['image'])
			instance.save()
			return HttpResponseRedirect(reverse('nnfoto.gallery.views.upload_file'))
	else:
		form = UploadFileForm()

	return 0
"""	