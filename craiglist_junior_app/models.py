from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"ID: {self.id} Name: {self.name}"


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE(), related_name='posts')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1024)

    def __str__(self):
        return f"ID: {self.id} and Title: {self.title}"