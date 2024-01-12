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
        
    
    