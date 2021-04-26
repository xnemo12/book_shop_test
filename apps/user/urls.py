from django.urls import path, re_path
from user.views import UserView, UserDetailView

urlpatterns = [
    re_path(r'^user/$', UserView.as_view(), name='user_view'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail_view'),
]
