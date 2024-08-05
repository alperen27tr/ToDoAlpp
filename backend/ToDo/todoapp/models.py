from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class TodoContent(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='todos', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
