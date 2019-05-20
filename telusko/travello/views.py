from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    dest = Destination()
    dest.name = 'Mumbai'
    dest.description = 'City Of Gold'
    dest.price = 700

    return render(request,"index.html",{'destt': dest})