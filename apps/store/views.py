from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.pagination import ResultsSetPagination
from core.permissions import HasSubscription
from store.models import Book
from store.serializers import BookSerializer


class BookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = ResultsSetPagination
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ['-pk']
    permission_classes = (AllowAny,)


class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated, HasSubscription)
