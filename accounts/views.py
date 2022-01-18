from accounts.models import UData
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render
from .models import User
from .forms import MyForm
from FRS.models import Interest,Customer,FriendRelation
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from FRS.models import Profile

# Create your views here.

def landing(request):
    return render(request,'landing.html')


def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()

  print(form)  
  return render(request, 'userHelp.html', {'form': form})


@login_required
def logout_user(request):
    request.session.clear()
    auth.logout(request)
    return redirect('/accounts/login') 

@login_required
def home(request):
    return render(request , 'home.html',{'USER' :Profile.objects.get(user=request.user)})


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        
        profile_obj = UData.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')
        
        login(request , user)
        return redirect('/home')

    return render(request , 'login.html')


def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            prof_obj= Profile(user=user_obj)
            int_obj=Interest(user=user_obj)
            cus_obj=Customer(user=user_obj)
            user_obj.save()    
            auth_token = str(uuid.uuid4())
            profile_obj = UData.objects.create(user = user_obj , auth_token = auth_token)
            prof_obj.save()
            profile_obj.save()
            int_obj.save()
            cus_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)
    else:
        return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = UData.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def suggest(request):
    p=request.GET['int']
    d=[]
    a=[]
    alfr=[]
    user=request.user
    Cust=Customer.objects.get(user=user)
    alfriends=FriendRelation.objects.filter(Friend1=Cust)
    for i in alfriends:
        alfr.append(i.Friend2.user)
    if p=="sports":
        IN=Interest.objects.filter(Sports=True)
        for i in IN:
            x=i.user_id
            a.append(i)
            d.append(User.objects.get(id=x))
        l=[]
        for j in d:
            pro=Profile.objects.get(user=j)
            l.append(pro)

        context={'a':a,'l':l,'alfr':alfr}
        return render(request,'suggestion.html',context)
    if p=="health":
        IN=Interest.objects.filter(Healthansfitness=True)
        for i in IN:
            x=i.user_id
            a.append(i)
            d.append(User.objects.get(id=x))
        l=[]
        for j in d:
            pro=Profile.objects.get(user=j)
            l.append(pro)

        context={'a':a,'l':l,'alfr':alfr}
        return render(request,'suggestion.html',context)   
     
    if p=="gardening":
        IN=Interest.objects.filter(Gardening=True)
        for i in IN:
            x=i.user_id
            a.append(i)
            d.append(User.objects.get(id=x))

        l=[]
        for j in d:
            pro=Profile.objects.get(user=j)
            l.append(pro)

        context={'a':a,'l':l,'alfr':alfr}
        return render(request,'suggestion.html',context)  
    if p=="photography":
        IN=Interest.objects.filter(Photography=True)
        for i in IN:
            x=i.user_id
            a.append(i)
            d.append(User.objects.get(id=x))

        l=[]
        for j in d:
            pro=Profile.objects.get(user=j)
            l.append(pro)

        context={'a':a,'l':l,'alfr':alfr}
        return render(request,'suggestion.html',context) 
    if p=="mentorship":
        IN=Interest.objects.filter(Mentorship=True)
        for i in IN:
            x=i.user_id
            a.append(i)
            d.append(User.objects.get(id=x))

        l=[]
        for j in d:
            pro=Profile.objects.get(user=j)
            l.append(pro)

        context={'a':a,'l':l,'alfr':alfr}
        return render(request,'suggestion.html',context)            

    
def friendship(request,**friend):
    find=friend['data']
    f=User.objects.get(username=find)
    FR=Customer.objects.get(user=f)
    user=request.user
    US=Customer.objects.get(user=user)
    friends1=FriendRelation(Friend1=US,Friend2=FR)
    friends2=FriendRelation(Friend1=FR,Friend2=US)
    friends1.save()
    friends2.save()
    messages.success(request,f'{f} added in friend list Sucessfully!!!')
    return redirect(request. META['HTTP_REFERER'])

def showfriends(request):
    friends=[]
    user=request.user
    Cust=Customer.objects.get(user=user)
    alfriends=FriendRelation.objects.filter(Friend1=Cust)
    for i in alfriends:
        x=i.Friend2.user
        pro=Profile.objects.get(user=x)
        friends.append(pro)
    print(friends)
    return render(request,'friends.html',{'friends':friends})
    

