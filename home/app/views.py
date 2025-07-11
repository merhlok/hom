from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from app.models import Product,Review

@api_view(['GET'])
def product(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    product = Product.objects.all()
    ser =  ProductListSerializer(product, many=True)
    return Response(ser.data)




class ProductDetailsView(APIView):
    def get(self, request,pk):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"error": "Товар не найден"},
                status= status.HTTP_404_NOT_FOUND
            )
            
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)

# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass