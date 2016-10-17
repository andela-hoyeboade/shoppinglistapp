from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from shop.models import ShoppingList


class TestShop(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='hassan', password='hassan')
        self.user.set_password('hassan')
        self.user.save()
        self.client = Client()
        self.client.login(username='hassan', password='hassan')
        self.create_shopping_list()

    def create_shopping_list(self, name='Wears'):
        self.shoplist = ShoppingList.objects.create(
            name='Wears', owner=self.user)

    def test_can_retrieve_shooping_items(self):
        response = self.client.get(reverse('shop_list'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.shoplist, response.context_data.get('shoplists'))
