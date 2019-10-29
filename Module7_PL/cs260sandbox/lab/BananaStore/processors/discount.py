from django.conf import settings

def discount(request):
    return {'DISCOUNT': settings.DISCOUNT}
