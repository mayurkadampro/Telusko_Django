from django.db import models

# Create your models here.
class Destination:
    id : int
    name : str
    description : str
    image: str
    price : int
