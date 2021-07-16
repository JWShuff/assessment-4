from craiglist_junior_app.models import Category
from django.urls import path
from . import views


urlpatterns = [
    # - `/categories`: A page listing all the categories
    path('', views.category_list, name='home'),
    # - `/categories/:category_id`: A page to view the detail of a specific category and a list of all of its associated posts
    path('<int:category_id>/', views.category_detail, name='category_detail'),
    # - `/categories/new`: A page with a form to create a new category
    path('new/', views.new_category, name='new_category'),
    # - `/categories/:category_id/edit`: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here. 
    path('<int:category_id>/edit/', views.edit_category, name='edit_category'),
    # Path to POST a delete for a category:
    path('<int:category_id>/delete/', views.delete_category, name='delete_category'),
    # - `/categories/:category_id/posts/new`: A page with a form to create a new post, under the current category by default.
    path('<int:category_id>/posts/new', views.new_post, name='new_post'),
    # - `/categories/:category_id/posts/:post_id`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/:category_id/`)
    path('<int:category_id>/posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # - `/categories/:category_id/posts/:post_id/edit`: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.
    path('<int:category_id>/posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:category_id>/posts/<int:post_id>/edit/', views.delete_post,name='delete_post'),
]

