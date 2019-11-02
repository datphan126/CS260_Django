from django.shortcuts import render
from . import forms, models
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import sys

# Create your views here.


def add_product(request):
    form_title = "Add a new product"
    success_message = "The product has been edited!"
    error_message = "Failed to edit the product! Please check the error message(s)."

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
                models.create_process(
                    name, price, nutrition, origin, product_image)
                action = 'SUCCESSFUL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'ERROR'
            except:
                print("Unexpected error: " + str(sys.exc_info()[0]))
                form.add_error(
                    None, 'Unexpected error - Please contact your system administrator')
                action = 'ERROR'
        else:
            action = 'ERROR'
    else:
        action = 'GET'
        # Disable auto_id to prevent the form from generating verbose information.
        # Also, we set the initial value to the album image field
        form = forms.ProductForm(auto_id=False, initial={
                                 'product_image': 'http://'})
        # Reference is now an unbound (empty) form
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request, 'product/product_form.html', {'action': action, 'form': form, 'form_title': form_title, 'success_message':success_message,'error_message':error_message})


def get_all_products(request):
    product_dict = models.fetch_all_products_process()

    return render(request, 'homepage.html', {'product_dict': product_dict})


def edit_product(request):
    id = request.POST.get('id', '')

    # If id doesn't exist, redirect to the homepage
    if(id == ''):
        return HttpResponseRedirect('/')

    form_title = "Edit song"
    success_message = "The product has been edited!"
    error_message = "Failed to edit the product! Please check the error message(s)."
    # Create an empty form so that Django doesn't complaint
    form = forms.ProductForm()

    if('popup' in id):
        action = ''

        # Clean up the id
        id = id.replace('popup', '')

        try:
            # Fetch the item from the DB based on the given id, and then populate the fields
            product = models.fetch_one_product_process(id)
            form = forms.ProductForm(auto_id=False, initial={'id': product.id, 'name': product.name,
                                                             'price': product.price, 'nutrition': product.nutrition, 'origin': forms.searchOriginsForKey(product.origin),
                                                             'product_image': product.product_image})
        except ValidationError as err:
            for err in err.messages:
                form.add_error(None, err)
            action = 'ERROR'
        except:
            print('Unexpected error: ' + str(sys.exc_info()[0]))
            action = 'ERROR'
    else:
        form = forms.ProductForm(request.POST)
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            # Extract form values
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            nutrition = form.cleaned_data['nutrition']
            origin = forms.ORIGIN[int(form.cleaned_data['origin'])][1]
            product_image = form.cleaned_data['product_image']

            try:
                models.edit_process(
                    id, name, price, nutrition, origin, product_image)
                action = 'SUCCESSFUL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'ERROR'
            except:
                print("Unexpected error: " + sys.exc_info()[0])
                form.add_error(
                    None, 'Unexpected error - Please contact your system administrator')
                action = 'ERROR'
        else:
            action = 'ERROR'

    return render(request, 'product/product_form.html', {'action': action, 'form': form, 'form_title': form_title, 'success_message':success_message,'error_message':error_message})


def delete_product(request):

    id = request.POST.get('id', '')
    if(id == ''):
        return HttpResponseRedirect('/')
    else:
        id = id.replace('popup', '')

    try:
        models.delete_process(id)
    except:
        print("Unexpected error: " + sys.exc_info()[0])

    return HttpResponseRedirect('/')
