from django.shortcuts import render

# Create your views here.


def pay(request, product="BananaChips"):
    price = request.GET.get('price', 'N/A')
    nutrition = request.GET.get('nutrition', 'N/A')
    origin = request.GET.get('origin', 'N/A')
    # Create an information dictionary
    info = {'product': product, 'price': price,
            'nutrition': nutrition, 'origin': origin}
    return render(request, 'product/details.html', {'info': info})
