from django.forms import ModelForm, RadioSelect
from django.contrib.auth.models import User
from posts.models import *

class HighlightForm(ModelForm):
  class Meta:
    model = Highlight
    exclude = ('user','has_been_hashed')
    widgets = {
      'emotion': RadioSelect(attrs={})
    }