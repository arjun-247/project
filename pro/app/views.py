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
    return render(request,'men.html')