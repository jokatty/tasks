import py_compile
from django import path
from . import views

urlpatterns = [
  path('', views.index)
]