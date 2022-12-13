from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# views
def index(request):
  # return HttpResponse("hi")
  # get data from todo table
  todos = Todo.objects.all()
  form = TodoForm()
  context = {'todos': todos, 'form':form}
  return render(request,'todo/list.html', context)
