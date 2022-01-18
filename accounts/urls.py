from django.contrib import admin
from django.urls import path
from .views import *
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from .views import logout as lg
from django.contrib import admin
from django.urls import path
from .views import *
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.landing,name='landing'),
    path('home' ,  views.home  , name="home"),
    path('form', views.my_form, name='form'),
    path('register/' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('logout/',logout_user,name="logout"),
    path('suggest/',suggest,name="suggest"),
    path('friendship/<str:data>',friendship,name="friendship"),
    path('showfriends/',showfriends,name='showfriends'),
    path('reset-password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset-password-sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset-password-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete")
]
urlpatterns += staticfiles_urlpatterns()