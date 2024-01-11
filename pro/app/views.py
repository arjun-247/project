from django.shortcuts import render

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
def women(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'women.html',data)
def kids(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'kids.html',data)