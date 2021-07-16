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
    else:
        form=CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form':form, 'type_of_request':"Edit"})

def delete_category(request, category_id):
    if request.method=='POST':
        category=get_category(category_id)
        category.delete()
    return redirect('home')

# Post Methods
def post_detail(request, category_id, post_id):
    try:
        post = get_post(post_id)
        category=get_category(category_id)
    except:
        return HttpResponse(f"Post with ID {post_id} does not exist.")
    return render(request, 'posts/post_detail.html', {'post':post, 'category':category})
    

def new_post(request, category_id):
    category = get_category(category_id)
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', post_id=post.id, category_id=category.id)
    else:
        initial_form = {'title':'Post title here', 'content':'Write your post here', 'category':category} 
        form = PostForm(initial = initial_form)
    

    return render(request,'posts/post_form.html', {'form':form, 'type_of_request':'New'})

        

def edit_post(request, category_id, post_id):
    return HttpResponse("Edit Post Form!")

def delete_post(request, category_id, post_id):
    return HttpResponse("Delete Post Success")

