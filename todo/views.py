from django.shortcuts import render
from django import HttpResponse

# views

def index(request):
  return HttpResponse("hi")
