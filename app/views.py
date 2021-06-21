from django.shortcuts import render
from django.http import JsonResponse
from . import services
from . import models

def index(request):
    return render(request, 'app/index.html')

def findFibonachiInt(request):
    """
    находим ближайшее число из фибоначчи
    сохраняем input и output
    возвращяем output
    """
    int_for_search = request.GET.get('int_for_search')
    fib_int = services.findIntByFibonachi(int_for_search)
    fibonachi = models.Fibonachi()
    fibonachi.input = int_for_search
    fibonachi.output = fib_int
    fibonachi.save()
    return JsonResponse({'output':fib_int})
