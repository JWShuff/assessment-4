from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Post

def get_category(category_id):
    return Category.objects.get(id=category_id)

def get_post(post_id):
    return Post.objects.get(id=post_id)

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories':categories})

def category_detail(request, category_id):
    return HttpResponse(f"Yep, category id {category_id} is working.")