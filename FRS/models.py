from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from PIL import Image
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MobileNumber = models.CharField(max_length=10,default=0000000000)
    DateTime=models.DateTimeField(default=timezone.now) #Date once added cannot be changed
    Age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class FriendRelation(models.Model):
    Friend1 = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='Friend1_set')
    Friend2 = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='Friend2_set')
    
    def __str__(self):
        return f'{self.Friend1.user.username} has friendship with {self.Friend2.user.username}'


class Interest(models.Model):
    title = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='InterestUser')
    Photography = models.BooleanField(default=False)
    Healthansfitness = models.BooleanField(default=False)
    Mentorship = models.BooleanField(default=False)
    Gardening = models.BooleanField(default=False)
    Sports = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='ProfileUser')
    image = models.ImageField(default='anonymous.jpeg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)