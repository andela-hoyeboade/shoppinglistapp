from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^$', views.ShopListView.as_view(), name='shop_list'),
]
