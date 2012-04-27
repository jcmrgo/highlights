from django.db import models
from django.contrib.auth.models import User


class highlight(models.Model):
	"""main object of app"""
	user = models.ForeignKey(User, related_name='user')
	text = models.TextField("highlight ", max_length=140, help_text="What's up?")


	def __init__(self, arg):
		super(highlight, self).__init__()
		self.arg = arg
		
