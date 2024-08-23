from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def sum_numbers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        result = sum(data['numbers'])
        return JsonResponse({'result': result})

@csrf_exempt
def average_numbers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        numbers = data['numbers']
        result = sum(numbers) / len(numbers)
        return JsonResponse({'result': result})

@csrf_exempt
def product_numbers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = 1
        for number in data['numbers']:
            product *= number
        return JsonResponse({'result': product})