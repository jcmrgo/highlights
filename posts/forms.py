from django.contrib.auth.models import User

class LoginForm(ModelForm):
  class Meta:
    model = User
    fields = ('email','password')