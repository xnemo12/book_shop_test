from django.urls import path, re_path
from store.views import BookView, BookDetailView

urlpatterns = [
    re_path(r'^book/$', BookView.as_view(), name='book_view'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail_view'),
]
