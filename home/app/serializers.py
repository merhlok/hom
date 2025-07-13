from rest_framework import serializers
from app.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta: 
        model = Book
        fields =['author', 'title', 'year']
    pass
    





class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    reviews = BookSerializer(many=True)
    class Meta: 
        model = Order
        fields =['user_name', 'days_count', 'date', 'books']

 