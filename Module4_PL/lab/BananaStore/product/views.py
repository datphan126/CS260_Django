from django.shortcuts import render
from django.template.response import TemplateResponse
from django.conf import settings

# Create your views here.


def product(request, product="BananaChips"):
    discount = settings.DISCOUNT

    price = request.GET.get('price', 'N/A')
    calories = request.GET.get('nutrition', 'N/A')
    origin = request.GET.get('origin', 'N/A')
    prices = ((0, price), (1, float(price)*float((100-discount)/100)))
    nutritionFacts = [calories, 10, 20, 30]
    # Create an information dictionary
    info = {'product': product, 'prices': prices,
            'nutritionFacts': nutritionFacts, 'origin': origin}
    return TemplateResponse(request, 'product/details.html', {'info': info})
