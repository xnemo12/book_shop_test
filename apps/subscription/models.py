import datetime

from django.db import models

from subscription.managers.subscription import SubscriptionManager
from user.models import User


class SubscriptionType(models.TextChoices):
    TEST = 'TEST', 'Test'
    MONTH = 'MONTH', 'Month'
    YEAR = 'YEAR', 'Year'


class Subscription(models.Model):
    start_date = models.DateField('Subscription started date')
    end_date = models.DateField('Subscription end date')
    user = models.ForeignKey(User, related_name='subscriptions', on_delete=models.SET_NULL, null=True)
    type = models.CharField('Subscription type', choices=SubscriptionType.choices, default=SubscriptionType.TEST,
                            max_length=5, null=True, blank=True)

    objects = SubscriptionManager()

    def is_active(self):
        return self.end_date <= datetime.datetime.now()
