from django.http import Http404
from django.shortcuts import render

from app.models import Car


from django.http import Http404
from django.shortcuts import render

from app.models import Car

def cars_list_view(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
        'total_cars': cars.count(),
    }
    
    return render(request, 'main/list.html', context)

def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = car.sales.all()
        context = {
            'car': car,
            'car_age': car.year,
            'recent_sales': sales,
        }
        
        return render(request, 'main/details.html', context)
        
    except Car.DoesNotExist:
        raise Http404('Автомобиль не найден')

def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = car.sales.all().order_by('-created_at')
        context = {
            'car': car,
            'sales': sales,
        }
        
        return render(request, 'main/sales.html', context)
        
    except Car.DoesNotExist:
        raise Http404('Автомобиль не найден')