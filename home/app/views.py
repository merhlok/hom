from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Order
from .serializers import BookSerializer,OrderSerializer


@api_view(['GET'])
def books_list(request):
    """получите список книг из БД
    отсериализуйте и верните ответ
    """
    i_book = Book.objects.all()
    serializer = BookSerializer(i_book, many=True)
    return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request):
        # получите данные из запроса
        serializer = BookSerializer(data=request.data) #передайте данные из запроса в сериализатор
        if serializer.is_valid(raise_exception=True): #если данные валидны
            return Response('Книга успешно создана') # возвращаем ответ об этом


class BookDetailsView(RetrieveAPIView):
    # реализуйте логику получения деталей одного объявления
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookUpdateView(UpdateAPIView):
    # реализуйте логику обновления объявления
     def patch(self, request, book_id):
        #пытаемся получить запись по id
        try:
            book = Book.objects.get(id=book_id)
            #получаем обновлённые данные из запроса
            data = request.data
            # сериализуем полученный объект
            serializer = BookSerializer(book, data=data)
            if serializer.is_valid():
                #проверяем валидны ли данные, если да, то сохраняем
                serializer.save()
                # выдаём в ответе сериализованный объект с обновленными данными 
                return Response(serializer.data)
            # если данные не валидны, то выдаём ошибку
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # если объект с указанной id не найден
        except Book.DoesNotExist:
            # выдаём 404
            return Response({"message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)

class BookDeleteView(DestroyAPIView):
    # реализуйте логику удаления объявления
    def delete(self, request, book_id):
        #пытаемся получить запись по id
        try:
            book = Book.objects.get(id=book_id)
            # если объект есть, то удаляем его
            book.delete()
            # выдаём пользователю ответ
            return Response({"message": "Запись успешно удалена"})
        # если объект с указанной id не найден
        except Book.DoesNotExist:
            # выдаём 404
            return Response({"message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)


class OrderViewSet(viewsets.ModelViewSet):
    # реализуйте CRUD для заказов
    queryset = Order.objects.all()
    serializer_class = OrderSerializer