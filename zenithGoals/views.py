from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  # return HttpResponse('Hello World ! Im home .')
  return render(request,'home.html')


def about(request):
  # return HttpResponse('this is our about page. ')
  return render(request,'about.html')