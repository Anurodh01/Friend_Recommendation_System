from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class UData(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
 
class user(models.Model):
    user_id=models.AutoField
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField(max_length=50)
    user_msg=models.TextField(max_length=200, default= "Add your feedback  here")

    def get_absolute_url(self):
        return reverse('accounts:landing')  
