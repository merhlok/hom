from rest_framework import serializers
from app.models import Review,Product

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["mark","text"]


class ProductListSerializer(serializers.Serializer):
    prise = serializers.CharField()
    title = serializers.CharField()


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Review
        fields = ['title',' description', 'price','reviews']