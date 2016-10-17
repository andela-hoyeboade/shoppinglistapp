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

    def test_user_can_create_new_shopping_list(self):
        response = self.client.post(reverse('shop_list_create'),
                                    {'name': 'Boots'})

        # Test redirection to all shopping list view
        self.assertEqual(response.status_code, 302)

        # Test shopping list is saved
        self.assertTrue(ShoppingList.objects.filter(
            name='Boots', owner=self.user))
