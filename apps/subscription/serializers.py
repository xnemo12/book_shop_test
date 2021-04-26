from datetime import datetime, timedelta

from rest_framework import serializers

from subscription.models import Subscription, SubscriptionType


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('id', 'type')

    def create(self, validated_data):
        end_date = datetime.now() + timedelta(14)

        if validated_data.get('type') == SubscriptionType.MONTH:
            end_date = datetime.now() + timedelta(30)

        if validated_data.get('type') == SubscriptionType.YEAR:
            end_date = datetime.now() + timedelta(365)

        subscription = Subscription(**validated_data)
        subscription.start_date = datetime.now()
        subscription.start_date = end_date
        subscription.save()

        return subscription

