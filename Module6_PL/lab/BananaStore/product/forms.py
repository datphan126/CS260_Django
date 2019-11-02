from django import forms
from datetime import date

ORIGIN = ((0, 'Brazil'), (1, 'Italia'), (2, 'Thailand'),
          (3, 'Russia'), (4, 'Vietnam'), (5, 'Other'))


class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()
    nutrition = forms.CharField()
    origin = forms.ChoiceField(choices=ORIGIN)
    product_image = forms.URLField()
    # Override the default field order, which is the declaration order
    field_order = ['name', 'price', 'nutrition','origin','product_image']
