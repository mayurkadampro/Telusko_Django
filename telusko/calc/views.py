from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"main.html",{'name':'MIGHTY'})

def bye(request):
    return HttpResponse("Bye Bye")

def add(request):
    var1 = int(request.GET["numOne"])
    var2 = int(request.GET["numTwo"])
    res = var1 + var2
    return render(request,"result.html",{'result':res})

def multiply(request):
    var1 = int(request.GET["numOne"])
    var2 = int(request.GET["numTwo"])
    res = var1 * var2
    return render(request,"result.html",{'result':res})

def Dividation(request):
    var1 = int(request.POST["numOneD"])
    var2 = int(request.POST["numTwoD"])
    res = var1 / var2
    return render(request,"result.html",{'result':res})

