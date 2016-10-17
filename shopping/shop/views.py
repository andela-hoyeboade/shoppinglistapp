from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class ShopList(LoginRequiredMixin, TemplateView):
    template_name = 'shop/shop_list.html'
