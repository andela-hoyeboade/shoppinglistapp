from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase


class TestAccount(TestCase):

    def setUp(self):
        User.objects.create(username='hassan', password='hassan')
        self.client = Client()

    def test_user_can_login_with_valid_details(self):

        # Login with details
        response = self.client.post(reverse('index'),
                                    {'username': 'hassan',
                                     'password': 'hassan'})

        # Test redirection to shopping list view
        self.assertEqual(response.status_code, 302)
