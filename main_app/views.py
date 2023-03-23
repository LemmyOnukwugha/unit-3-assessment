from django.shortcuts import render, redirect


from django.shortcuts import render
from django.db.models import Sum
from .models import Widget

# Create your views here.


def home(request):
  widget_list= Widget.objects.all()
  sum = Widget.objects.aggregate(Sum('quantity'))
  
  return render(request, 'home.html', {'widget_list': widget_list, 'sum': sum})


def createWidget (request):
  item = Widget.objects.create (
    description = request.POST['description'],
    quantity = request.POST['quantity'],
  )
  return redirect ("/")

def deleteWidget (request, widget_id):
  Widget.objects.get (id=widget_id).delete()
  
  return redirect ("/")
