from craiglist_junior_app.models import Category
from django.urls import path
from . import views


urlpatterns = [
# - `/categories`: A page listing all the categories
    path('', views.home, name='home'),
# - `/categories/:category_id`: A page to view the detail of a specific category and a list of all of its associated posts
    path('<int:category_id>/', views.category_detail, name='category_detail'),
]


# - `/categories/new`: A page with a form to create a new category
# - `/categories/:category_id/edit`: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here. 
# - `/categories/:category_id/posts/new`: A page with a form to create a new post, under the current category by default.
# - `/categories/:category_id/posts/:post_id`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/:category_id/`)
# - `/categories/:category_id/posts/:post_id/edit`: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.