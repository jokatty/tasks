from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# views
def index(request):
  # return HttpResponse("hi")
  # get data from todo table
  todos = Todo.objects.all()
  form = TodoForm()
  #handle post request
  if request.method=='POST':
    form = TodoForm(request.POST)
    #check if the form has valid data and save it
    if form.is_valid():
      form.save()
    return redirect('/')
  context = {'todos': todos, 'form':form}
  return render(request,'todo/list.html', context)
