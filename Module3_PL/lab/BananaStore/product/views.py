from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.


def product(request, product="BananaChips"):
    price = request.GET.get('price', 'N/A')
    calories = request.GET.get('nutrition', 'N/A')
    origin = request.GET.get('origin', 'N/A')
    prices = ((0,price),(1,float(price)*0.7))
    nutritionFacts = [calories,10,20,30]
    # Create an information dictionary
    info = {'product': product, 'prices': prices,
            'nutritionFacts': nutritionFacts, 'origin': origin}
    return TemplateResponse(request, 'product/details.html', {'info': info})
