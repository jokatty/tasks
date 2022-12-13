from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# views
def index(request):
  # return HttpResponse("hi")
  # get data from todo table
  todos = Todo.objects.all()
  context = {'todos': todos}
  return render(request,'todo/list.html', context)
