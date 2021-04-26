from datetime import datetime

from django.db import models
from django.db.models import QuerySet


class SubscriptionManager(models.Manager):

    def get_active_subscriptions(self) -> QuerySet:
        queryset = self.get_queryset()
        queryset = queryset.filter(end_date__gte=datetime.now())
        return queryset
