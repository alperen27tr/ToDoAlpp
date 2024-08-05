from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, CategorySerializer, TodoContentSerializer
from .models import User, Category, TodoContent
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TodoContentViewSet(viewsets.ModelViewSet):
    queryset = TodoContent.objects.all()
    serializer_class = TodoContentSerializer

    def list(self, request, *args, **kwargs):
        print("list fonksiyonu çalıştı")
        category_id = request.query_params.get('category_id')  # Kategori ID'sini al
        print(category_id) #kategori id gelmiyor
        # Tüm verileri al
        queryset = self.filter_queryset(self.get_queryset())
        # Eğer category_id parametresi varsa, filtreyi uygula
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Tüm kullanıcıları al
    serializer_class = UserSerializer  # Kullanıcı verilerini serialize etmek için UserSerializer kullan

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()  # Kullanıcıyı kaydet
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Kullanıcıyı güncelle
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # Kullanıcıyı sil
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def list(self, request, *args, **kwargs):
    #     print("list fonksiyonu calisti")
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     if queryset.category_id:
    #          queryset = queryset.filter(category_id=queryset.category_id)
    #          print(queryset)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
#görev oluşturma (çalışmıyor)
@api_view(['POST'])
def CreateToDo(request):
    if request.method == 'POST':
        serializer = TodoContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Görev başarıyla oluşturuldu"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Geçersiz istek methodu"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def CreateToDoCategory(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Kategori başarıyla oluşturuldu"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Geçersiz istek methodu"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)