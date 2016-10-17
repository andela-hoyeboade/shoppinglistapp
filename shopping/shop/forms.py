from django import forms
from shop.models import ShoppingList


class ShopListForm(forms.ModelForm):

    class Meta:
        model = ShoppingList
        exclude = ['owner']
