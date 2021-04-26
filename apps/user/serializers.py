import datetime

from rest_framework import serializers

from subscription.models import Subscription, SubscriptionType
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        now = datetime.datetime.now()
        Subscription.objects.create(
            start_date=now,
            end_date=now + datetime.timedelta(14),
            type=SubscriptionType.TEST,
            user=user
        )

        return user
