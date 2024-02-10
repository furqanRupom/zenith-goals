from django.shortcuts import render
from .models import Post
from django.http import HttpResponse;

# Create your views here.

def posts_list(request):
  # this way we can do fetching data in django orm
  posts = Post.objects.all().order_by('-date')
  return render(request,'posts/posts_list.html',{'posts':posts})


def post_page(request,slug):
  post = Post.objects.get(slug=slug)
  return render(request,'posts/post_page.html',{'post':post})