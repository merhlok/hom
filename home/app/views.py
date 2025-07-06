from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def cook(request, name, count=1):
    if name in DATA:
        recipe = DATA[name].copy()
        for ingredient in recipe:
            recipe[ingredient] *= count
        context = {'page': recipe}
    else:
        context = {'page': {}}
    
    return render(request, 'home.html', context)