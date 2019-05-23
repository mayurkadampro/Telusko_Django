from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.description = 'City Of Gold'
    dest1.price = 700
    dest1.image = "destination_1.jpg"
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Goa'
    dest2.description = 'Enjoy Ur Holidays'
    dest2.price = 900
    dest2.image = "destination_2.jpg"
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.description = 'A place which teaches us to chill.'
    dest3.price = 800
    dest3.image = "destination_3.jpg"
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'singapore'
    dest4.description = 'Passion Made Possible'
    dest4.price = 1000
    dest4.image = "destination_4.jpg"
    dest4.offer = True

    distt = [dest1,dest2,dest3,dest4]

    return render(request,"index.html",{'destt': distt})