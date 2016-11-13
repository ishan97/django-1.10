from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import shortenURL
# Create your views here.
def shorten_redirect_view(request, shortcode=None, *args, **kwargs): #This is a function based View FBV
	
	obj = get_object_or_404(shortenURL, shortcode=shortcode)
		#other methods-->
	# try:
	# 	obj=shortenURL.objects.get(shortcode=shortcode)
	# except:
	# 	obj=shortenURL.objects.all().first()
		#2nd method-->

	# obj_url=None
	# qs=shortenURL.objects.filter(shortcode_iexact=shortcode.upper())
	# if qs.exists() and qs.count() = 1:
	# 	obj = qs.first()
	# 	obj_url=obj.url
	# return HttpResponse("hello {sc}".format(sc=obj_url))	

	return HttpResponseRedirect(obj.url)

class shortenCBView(View): #class based view CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(shortenURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)

	def post(self, request, *args, **kwargs):
		return HttpResponse()