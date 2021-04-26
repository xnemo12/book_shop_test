from django.urls import path, include

urlpatterns = [
    path('', include('user.urls')),
    path('', include('store.urls')),
    path('', include('subscription.urls')),
]