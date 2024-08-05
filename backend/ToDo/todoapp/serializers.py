from rest_framework import serializers
from .models import User, Category, TodoContent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TodoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoContent
        fields = '__all__'
