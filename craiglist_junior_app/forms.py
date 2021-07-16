from django import forms
from django.forms import widgets
from .models import Category, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=('name','description')
        widgets= {
            'name': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title', 'content', 'category')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'content':forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            ),
        }