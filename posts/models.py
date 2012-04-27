from django.db import models
from django.contrib.auth.models import User
import re

EMOTION_CHOICES = (
	(1, "Happy"),
	(2, "Sad"),
	(3, "Angry"),
)
BIGNESS_CHOICES = (
	(1, "Small Event"),
	(2, "Not So Big Event"),
	(3, "Big Event"),
	(4, "Major Event"),
	(5, "Super Major Event"),
)

class Highlight(models.Model):
	"""main object of app"""
	user = models.ForeignKey(User, related_name='user')
	text = models.TextField("highlight", max_length=140)
	emotion =  models.IntegerField(choices=EMOTION_CHOICES, default=1)
	bigness = models.IntegerField(choices=BIGNESS_CHOICES, default=3)
	date_created = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
	def __unicode__(self):
		return self.text

	def save(self, *args, **kwargs):
		super(Highlight, self).save(*args, **kwargs)
		patern = re.compile(r"#([A-Za-z0-9_]+)")
		hashtags = patern.findall(self.text)
		for ht in hashtags:
			highlight_ht = HighlightHashtag(highlight=self, hashtag=ht)
			highlight_ht.save()

class HighlightHashtag(models.Model):
	highlight = models.ForeignKey(Highlight)
	hashtag = models.CharField(max_length=60)
	def __unicode__(self):
		return self.hashtag
		
