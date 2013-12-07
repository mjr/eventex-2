# coding: utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subscribed_today.short_description = _(r'Inscrito hoje?')
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionAdmin)
