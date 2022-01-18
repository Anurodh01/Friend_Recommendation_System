from django import forms
from .models import user
 
class MyForm(forms.ModelForm):
  class Meta:
    model = user
    fields = ["user_email", "user_name","user_msg"]
    labels = {'user_email': "UserE-mail", "user_name": "User_Name","user_msg":"Query",}
