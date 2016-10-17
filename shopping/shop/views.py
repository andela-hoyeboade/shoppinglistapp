from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import TemplateView
from shop.forms import ShopListForm
from shop.models import ShoppingList


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
