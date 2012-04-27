from django.db import models
from django.utils.safestring import mark_safe
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
def hashtaggear(highlight):
	pattern = re.compile(r"(?P<start>.?)#(?P<hashtag>[A-Za-z0-9_]+)(?P<end>.?)")
	link = r'\g<start><a href="/search/\g<hashtag>"  title="#\g<hashtag> search Highlights">#\g<hashtag></a>\g<end>'
	text = pattern.sub(link,highlight)
	return mark_safe(text)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to="../highlights/media/users")

class Highlight(models.Model):
	"""main object of app"""
	user = models.ForeignKey(User, related_name='user')
	text = models.TextField("highlight", max_length=140)
	emotion =  models.IntegerField(choices=EMOTION_CHOICES, default=1)
	bigness = models.IntegerField(choices=BIGNESS_CHOICES, default=3)
	date_created = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
	share = models.BooleanField(default=False)
	has_been_hashed = models.BooleanField(default=False)
	def __unicode__(self):
		return self.text
	def save(self, *args, **kwargs):
		pattern = re.compile(r"#([A-Za-z0-9_]+)")
		hashtags = pattern.findall(self.text)
		if not self.has_been_hashed:
			self.text = hashtaggear(self.text)
			self.has_been_hashed = True
		super(Highlight, self).save(*args, **kwargs)
		for ht in hashtags:
			obj, created = HighlightHashtag.objects.get_or_create(highlight=self, hashtag=ht)
		

class HighlightHashtag(models.Model):
	highlight = models.ForeignKey(Highlight)
	hashtag = models.CharField(max_length=60)
	
	def __unicode__(self):
		return self.hashtag
		
