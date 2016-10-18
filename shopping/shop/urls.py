from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^$', views.ShopListView.as_view(), name='shop_list'),
    url(r'^create', views.ShopListCreateView.as_view(), name='shop_list_create'),
    url(r'^(?P<shop_list_id>[0-9]+)/items/create$', views.ShopListItemCreateView.as_view(),
        name='shop_list_item_create'),
    url(r'^(?P<shop_list_id>[0-9]+)/items$',
        views.ShopListItemView.as_view(), name='shop_list_items'),
    url(r'^(?P<shop_list_id>[0-9]+)/items/(?P<item_id>[0-9]+)/delete$',
        views.ShopListItemDeleteView.as_view(), name='shop_list_item_delete'),
    url(r'^(?P<shop_list_id>[0-9]+)/items/(?P<item_id>[0-9]+)/update$',
        views.ShopListItemUpdateView.as_view(), name='shop_list_item_update')

]
