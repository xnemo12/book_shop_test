from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from subscription.serializers import SubscriptionSerializer


class SubscriptionView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        user = self.request.user

        if user.has_active_subscription():
            return Response(
                {'user_id': user.id, 'status': 'error', 'msg': 'User already have active subscription'}, 400
            )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscription = serializer.save(user=user)
        return Response({'user_id': user.id, 'status': 'ok', 'period': subscription.type}, 201)
