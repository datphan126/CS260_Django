from django.shortcuts import render

# Create your views here.


def pay(request, product="BananaChips"):
    price = request.GET.get('price', 'N/A')
    calories = request.GET.get('calories', 'N/A')
    origin = request.GET.get('origin', 'N/A')
    # Create an information dictionary
    info = {'product': product, 'price': price,
            'calories': calories, 'origin': origin}
    return render(request, 'menu/details.html', {'info': info})
