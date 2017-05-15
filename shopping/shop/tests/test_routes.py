from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from shop.models import ShoppingList, ShoppingListItem


class TestShop(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='hassan', password='hassan')
        self.user.set_password('hassan')
        self.user.save()
        self.client = Client()
        self.client.login(username='hassan', password='hassan')
        self.create_shopping_list()
        self.create_shopping_list_item()

    def create_shopping_list(self, id=100, name='Wears'):
        self.shoplist = ShoppingList.objects.create(id=id,
                                                    name='Wears', owner=self.user)

    def create_shopping_list_item(self, id=100, name='Size 44 boot'):
        self.shoplist_item = ShoppingListItem.objects.create(id=id,
                                                             name=name,
                                                             shoplist=self.shoplist)

    def test_can_retrieve_shooping_items(self):
        response = self.client.get(reverse('shop_list'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.shoplist, response.context_data.get('shoplists'))

    def test_user_can_create_new_shopping_list(self):
        response = self.client.post(reverse('shop_list_create'),
                                    {'name': 'Boots',
                                     'budget': 1000})

        # Test redirection to all shopping list view
        self.assertEqual(response.status_code, 302)

        # Test shopping list is saved
        self.assertTrue(ShoppingList.objects.filter(
            name='Boots', owner=self.user))

    def test_user_can_add_items_to_shopping_list(self):
        response = self.client.post(reverse('shop_list_item_create', kwargs={'shop_list_id': 100}),
                                    {'name': '2 pairs of jeans'})

        # Test item is saved
        self.assertTrue(ShoppingListItem.objects.filter(
            name='2 pairs of jeans', shoplist=self.shoplist))

    def test_user_can_view_items_in_shopping_list(self):
        response = self.client.get(
            reverse('shop_list_items', kwargs={'shop_list_id': 100}))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.shoplist_item,
                      response.context_data.get('shoplistitems'))

    def test_can_set_budget_for_shopping_list(self):
        response = self.client.post(reverse('shop_list_create'),
                                    {'name': 'Groceries',
                                     'budget': 1500})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(ShoppingList.objects.filter(
            name='Groceries', budget=1500))
