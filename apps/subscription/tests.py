from datetime import datetime

from rest_framework.test import APITestCase
from django.urls import reverse

from subscription.models import SubscriptionType


class SubscriptionTest(APITestCase):

    def setUp(self):
        super(APITestCase, self).setUp()
        self.client.login(username='admin', password='123456')

    def test_create(self):
        response = self.client.post(reverse('subscription_view'), {
            'type': SubscriptionType.MONTH,
        })
        self.assertEqual(response.status_code, 201)

        response = self.client.post(reverse('regions_view'), {'type': 'Unknown'})
        self.assertEqual(response.status_code, 400)
