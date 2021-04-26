from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from core.pagination import ResultsSetPagination
from user.models import User
from user.serializers import UserSerializer
from rest_framework.response import Response


class UserView(ListCreateAPIView):
    serializer_class = UserSerializer
    pagination_class = ResultsSetPagination
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ['-pk']
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 201)


class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
