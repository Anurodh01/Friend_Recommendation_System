from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Interest, Profile


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget = forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class InterestUpdateForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['Photography','Healthansfitness','Mentorship','Gardening','Sports']

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Age','MobileNumber']