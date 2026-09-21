from django.shortcuts import render
from finance.models import Category
from finance.serializers import CategorySerializer
from rest_framework import mixins, generics, permissions

def home(request):
    return render(request, 'home.html')

class CategoryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
    