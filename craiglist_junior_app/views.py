from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Post
from .forms import CategoryForm, PostForm

def get_category(category_id):
    return Category.objects.get(id=category_id)

def get_post(post_id):
    return Post.objects.get(id=post_id)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories':categories})

def category_detail(request, category_id):
    category= get_category(category_id)
    return render(request, 'categories/category_detail.html', {'category':category})

def new_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            category=form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm
    return render(request, 'categories/category_form.html', {'form':form, 'type_of_request':'New'})

def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method=="POST":
        form=CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category=form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)

def delete_category(request, category_id):
    pass

# Post Methods

def new_post(request):
    pass

def post_detail(request, category_id, post_id):
    pass

def edit_post(request, category_id, post_id):
    pass

def delete_post(request, category_id, post_id):
    pass

