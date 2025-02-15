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
        try:                
            if form.is_valid():
                category=form.save(commit=False)
                category.save()
                return redirect('category_detail', category_id=category.id)
        except:
            return HttpResponse("Something has gone terribly wrong. Press back and yell at the Developer.")
    else:
        form = CategoryForm
    return render(request, 'categories/category_form.html', {'form':form, 'type_of_request':'New'})


def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method=="POST":
        form=CategoryForm(request.POST, instance=category)
        try: 
            if form.is_valid():
                category=form.save(commit=False)
                category.save()
                return redirect('category_detail', category_id=category.id)
        except:
            return HttpResponse("Something has gone terribly wrong in editing this category. Press back, and yell at the Developer.")
    else:
        form=CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form':form, 'type_of_request':"Edit"})


def delete_category(request, category_id):
    try:
            
        if request.method=='POST':
            category=get_category(category_id)
            category.delete()
    except:
        return HttpResponse("Something has gone terribly wrong in deleting this category. Yell at the Developer.")
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
        try:
            if form.is_valid():
                post=form.save(commit=False)
                post.category = category
                post.save()
                return redirect('post_detail', post_id=post.id, category_id=category.id)
        except:
            return HttpResponse("Something has gone terribly wrong in creating this post. Yell at the Developer.")
    else:
        initial_form = {
            'title':'Post title here',
            'content':'Write your post here', 
            'category':category} 
        form = PostForm(initial = initial_form)
    return render(request,'posts/post_form.html', {'form':form, 'type_of_request':'New', 'category':category})

        

def edit_post(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method=="POST":
        form=PostForm(request.POST, instance=post)
        try:
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('post_detail', post_id = post.id, category_id=category.id)
        except:
            return HttpResponse("Something has gone terribly wrong in editing this post. Yell at the Developer.")
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'type_of_request':"Edit", 'category':category, 'post':post})

def delete_post(request, category_id, post_id):
    if request.method=='POST':
        try:
            category=get_category(category_id)
            post=get_post(post_id)
            post.delete()
            return redirect('category_detail', category_id=category.id)
        except:
            return HttpResponse("Something has gone terribly wrong. Yell at the Developer.")

