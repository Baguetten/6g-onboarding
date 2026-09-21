from rest_framework import serializers
from finance.models import Category, Income, Expense

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = ['id', 'name', 'owner']

