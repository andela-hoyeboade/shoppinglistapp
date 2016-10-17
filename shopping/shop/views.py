from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django.views.generic import TemplateView
from shop.forms import ShopListForm, ShopListItemForm
from shop.models import ShoppingList, ShoppingListItem


class ShopListView(LoginRequiredMixin, TemplateView):
    template_name = 'shop/shop_list.html'

    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        context['shoplists'] = ShoppingList.objects.filter(
            owner=self.request.user)
        return context


class ShopListCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'shop/shop_create.html'
    formclass = ShopListForm

    def get_context_data(self, **kwargs):
        context = super(ShopListCreateView,
                        self).get_context_data(**kwargs)
        context['shoplistform'] = ShopListForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.formclass(request.POST)

        if form.is_valid():
            shoplist = form.save(commit=False)
            shoplist.owner = self.request.user
            shoplist.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Shoplist created successfully')
            return redirect(reverse('shop_list'),
                            context_instance=RequestContext(request))
        else:
            context = super(ShopListCreateView,
                            self).get_context_data(*args, **kwargs)
            context['shoplistform'] = form
            return render(request, self.template_name, context)


class ShopListItemCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'shop/shop_list_item_create.html'
    formclass = ShopListItemForm

    def get_context_data(self, **kwargs):
        context = super(ShopListItemCreateView,
                        self).get_context_data(**kwargs)
        context['shoplist'] = get_object_or_404(ShoppingList, id=kwargs.get('shop_list_id', 0),
                                                owner=self.request.user)
        context['shoplistitemform'] = ShopListItemForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.formclass(request.POST)
        shoplist = get_object_or_404(
            ShoppingList, id=kwargs.get('shop_list_id', 0), owner=self.request.user)
        if form.is_valid():
            shoplist_item = form.save(commit=False)
            shoplist_item.shoplist = shoplist
            shoplist_item.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Shoplist item created successfully')
            return redirect(reverse('shop_item_create', kwargs={'shop_list_id': shoplist.id}),
                            context_instance=RequestContext(request))
        else:
            context = super(ShopListItemCreateView,
                            self).get_context_data(*args, **kwargs)
            context['shoplist'] = get_object_or_404(ShoppingList, id=kwargs.get('shop_list_id', 0),
                                                    owner=self.request.user)
            context['shoplistitemform'] = form
            return render(request, self.template_name, context)
