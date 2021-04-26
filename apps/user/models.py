from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)
    date_of_birthday = models.DateField(_('date of birthday'), null=True, blank=True, )
    avatar = models.ImageField(null=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_active_subscription(self):
        return self.subscriptions.get_active_subscriptions().count() > 0
