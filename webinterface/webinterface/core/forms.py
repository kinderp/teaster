from django.forms import ModelForm

from .models import Bug
from .models import Product

class BugCreateForm(ModelForm):
    class Meta:
        model = Bug
        fields = ['name','description', 'product']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'version', 'product_type']
