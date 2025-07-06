from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
import os

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    # Полный путь к CSV-файлу (лучше вынести в настройки)
    file_path = r'C:\Users\Захарка\Desktop\NETO\home\data-398-2018-08-30.csv'
    

    
    # Чтение данных из CSV
    stations = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)  # Преобразуем в список словарей
    
    # Настройка пагинации
    paginator = Paginator(stations, 15)  # 15 станций на странице
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    
    context = {
        'bus_stations': page.object_list,  # Станции на текущей странице
        'page': page,  # Объект страницы для навигации
    }
    return render(request, 'index.html', context)
    
    