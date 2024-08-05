from django.urls import path,include
from .views import UserViewSet, CategoryViewSet, TodoContentViewSet,CreateToDo,CreateToDoCategory
from rest_framework.routers import DefaultRouter
from django.contrib import admin


router = DefaultRouter()    
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'todos', TodoContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-todo/', CreateToDo, name='create-todo'),
    path('admin/', admin.site.urls),
    path('create_category/', CreateToDoCategory, name='create_category'),
    ]