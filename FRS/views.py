from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Interest,Customer
from .forms import UserUpdateForm, ProfileUpdateForm,InterestUpdateForm,CustomerUpdateForm
from django.contrib.auth import authenticate,login,logout
from FRS.models import Profile

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=Profile.objects.filter(user=request.user).first())
        int_form=InterestUpdateForm(request.POST,instance=Interest.objects.filter(user=request.user).first())
        cus_form=CustomerUpdateForm(request.POST,instance=Customer.objects.filter(user=request.user).first())
        if u_form.is_valid() and p_form.is_valid() and int_form.is_valid():
            u_form.save()
            p_form.save()
            int_form.save()
            cus_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        int_form=InterestUpdateForm(instance=Interest.objects.filter(user=request.user).first())
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance = Profile.objects.filter(user=request.user).first())
        cus_form=CustomerUpdateForm(instance=Customer.objects.filter(user=request.user).first())
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'photo' :Profile.objects.filter(user=request.user).first().image,
        'int_form':int_form,
        'cus_form' :cus_form
    }

    return render(request, 'profile.html', context)