from __future__ import unicode_literals

from django.db import models

from .utils import code_generator, create_shortcode
from django.conf import settings
# Create your models here.

SHORTCODE_MAX=getattr(settings, 'SHORTCODE_MAX', 15)   #<== This ensures if available in settings or set the default value
#SHORTCODE_MAX=settings.SHORTCODE_MAX   				<== This can also be used but is not the best practise

class ShortenURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main=super(ShortenURLManager, self).all(*args, **kwargs)
		qs=qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items=None):
		qs=shortenURL.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs=qs.order_by('-id')[:items]
		new_codes=0
		for q in qs:
			q.shortcode=create_shortcode(q)
			print(q.id)
			q.save()
			new_codes+=1
		return "----new codes made {i}".format(i=new_codes)


class shortenURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True) #when model was created
	update    = models.DateTimeField(auto_now=True) #everytime model is updated
	active    = models.BooleanField(default=True)
	#shortcode = models.CharField(max_length=15, null=True)  ==> Empty in database is okay
	#shortcode = models.CharField(max_length=15, default='ishanDefault')
	objects=ShortenURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode= create_shortcode(self)
		super(shortenURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)


'''
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

'''
'''
ADDING USING SHELL==>

python manage.py shell 							<================ loads the shell
from shortener.models import shortenURL 		<================ imports the model
shortenURL.objects.all() 						<================ shows all
OR

obj=shortenURL.objects.create(url='', shortcode='')

'''