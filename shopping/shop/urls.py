from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^$', views.ShopListView.as_view(), name='shop_list'),
    url(r'^create', views.ShopListCreateView.as_view(), name='shop_list_create'),
    url(r'^(?P<shop_list_id>[0-9]+)/items/create', views.ShopListItemCreateView.as_view(),
        name='shop_item_create')
]
