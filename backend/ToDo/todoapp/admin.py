from django.contrib import admin
from .models import User, Category, TodoContent

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(TodoContent)
class TodoContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'user', 'category')
    list_filter = ('completed', 'user', 'category')
    search_fields = ('title', 'description')
