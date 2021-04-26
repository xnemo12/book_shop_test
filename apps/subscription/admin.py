from django.contrib import admin

from subscription.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'type', 'user')
    fields = ('start_date', 'end_date', 'type', 'user')
    search_fields = ('start_date', 'end_date', 'type', 'user')
