
from django.db import models



class TextRelations(models.Model):
    rel_from = models.ForeignKey('datastore.Sentiment', related_name='rel_from')
    rel_to = models.ForeignKey('datastore.Sentiment', related_name='rel_to')


class Sentiment(models.Model):
    text = models.CharField(max_length=255, blank=True)
    num_positive = models.IntegerField(default=0)
    num_negative = models.IntegerField(default=0)
    num_neutral = models.IntegerField(default=0)

    def get( self, request, format=None):
    	self.text = 'The Power of Django!!!'
    	return self  
    	# This is just a text for me to understand the inner workings
    	# Of how this framework talks to it's self

		


class Crawler(models.Model):
    ip_address = models.GenericIPAddressField(blank=False)
    is_active = models.BooleanField(default=True)

