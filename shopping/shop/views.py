from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from shop.models import ShoppingList


class ShopListView(LoginRequiredMixin, TemplateView):
    template_name = 'shop/shop_list.html'

    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        context['shoplists'] = ShoppingList.objects.filter(
            owner=self.request.user)
        return context
