from django.shortcuts import render
from django.template.response import TemplateResponse
from django.conf import settings
from . import forms, models
from django.core.exceptions import ValidationError
import sys

# Create your views here.


def add_product(request):
    form_title = "Add a new product"
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = forms.ProductForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            nutrition = form.cleaned_data['nutrition']
            origin = forms.ORIGIN[int(form.cleaned_data['origin'])][1]
            product_image = form.cleaned_data['product_image']
            
            try:
                models.create_process(name, price, nutrition, origin, product_image)
                action = 'POST_SUCCESSFULL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'POST_FAILED'
            except:
                print("Unexpected error: " + str(sys.exc_info()[0]))
                form.add_error(None,'Unexpected error - Please contact your system administrator')
                action = 'POST_FAILED'
        else:
            action='POST_FAILED'
    else:
        action='GET'
        # Disable auto_id to prevent the form from generating verbose information.
        # Also, we set the initial value to the album image field
        form = forms.ProductForm(auto_id=False,initial={'product_image':'http://'})
        # Reference is now an unbound (empty) form
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request,'product/product_form.html',{'action':action,'form':form,'form_title':form_title})

def get_all_products(request):
    product_dict = models.fetch_all_products_process()

    return render(request,'homepage.html', {'product_dict': product_dict})
