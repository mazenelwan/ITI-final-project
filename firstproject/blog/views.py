from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
 return render(request, 'blog/home.html')

def shop2(request):
 posts = Post.objects.filter(catagry="1")
 jackets = Post.objects.filter(catagry="2")
 tshirts = Post.objects.filter(catagry="4")
 polos = Post.objects.filter(catagry="5")
 shoes = Post.objects.filter(catagry="6")
 pants = Post.objects.filter(catagry="3")
 return render(request, 'blog/shop2.html', {
  "posts": posts,
  "jackets": jackets,
  "polos": polos,
  "shoes": shoes,
  "tshirts": tshirts,
  "pants": pants
 })


def contact(request):
 return render(request, 'blog/contact.html')

def about(request):
 return render(request, 'blog/about.html')