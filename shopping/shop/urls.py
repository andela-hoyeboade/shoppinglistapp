from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^$', views.ShopListView.as_view(), name='shop_list'),
    url(r'^create', views.ShopListCreateView.as_view(), name='shop_list_create')
]
