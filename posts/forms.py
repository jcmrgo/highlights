from django.forms import ModelForm
from django.contrib.auth.models import User
from posts.models import *

class HighlightForm(ModelForm):
  class Meta:
    model = Highlight
    exclude = ('user',)