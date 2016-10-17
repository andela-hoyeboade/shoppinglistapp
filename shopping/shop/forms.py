from django import forms
from shop.models import ShoppingList, ShoppingListItem


class ShopListForm(forms.ModelForm):

    class Meta:
        model = ShoppingList
        exclude = ['owner']


class ShopListItemForm(forms.ModelForm):

    class Meta:
        model = ShoppingListItem
        exclude = ['shoplist']
