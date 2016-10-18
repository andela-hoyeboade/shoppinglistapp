from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models


class Base(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ShoppingList(Base):
    name = models.CharField(max_length=50)
    budget = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='shoplists')

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shop_list_items', kwargs={'shop_list_id': self.pk})


class ShoppingListItem(Base):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    shoplist = models.ForeignKey(ShoppingList, related_name='items')

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shop_list_item_detail',
                            kwargs={'shop_list_id': self.shoplist.pk, 'item_id': self.pk})
