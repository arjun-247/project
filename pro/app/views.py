from django.shortcuts import render

from django.contrib import messages, auth

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# from .models import Watch
# from .forms import WatchForm
# from app.forms import*
# Create your views here.
from .models import Shoes

def index(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'index.html',data)


def men(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'men.html',data)
def men_casual(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'men_casual.html',data)
def men_formal(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'men_formal.html',data)
def men_boots(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'men_boots.html',data)
def men_sneakers(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'men_sneakers.html',data)


def women(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'women.html',data)
def women_casual(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'women_casual.html',data)

def women_dress(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'women_dress.html',data)

def women_sports(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'women_sports.html',data)



def kids(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'kids.html',data)
def collection(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'collection.html',data)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')


def details(request,id):
    p=Shoes.objects.get(pk=id)
    print(p)
    data={
        'data':p
    }
    return render(request,'product-detail.html',data)
        
    
def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass')
        password2=request.POST.get('cpass')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists!!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username=username,email=email,password=password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup.html')

def user_login (request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        print(username,password1)
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            messages.info(request,'user not exists')
            print('user no exist')
            return redirect(user_login)
    return render(request,'login.html')



def user_logout(request):
    logout(request)
    return redirect(index)