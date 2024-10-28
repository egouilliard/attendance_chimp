from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    fav_food = ['Chicken Wings', 'Pizza', 'Salt and Pepper Pork Chops']
    context = {'fav_food': fav_food}
    return render(request, 'app/index.html', context=context)
