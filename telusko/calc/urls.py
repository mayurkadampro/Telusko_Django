from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('bye',views.bye,name="bye"),
    path('add',views.add,name="add"),
    path('multiply',views.multiply,name="multiply"),
    path('Dividation',views.Dividation,name="Dividation")
]
