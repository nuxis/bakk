from django.contrib import admin

from .models import BadgeAccess, BadgeAccessLog


@admin.register(BadgeAccess)
class BadgeAccessAdmin(admin.ModelAdmin):
    list_display = ('card', 'description', 'active', )


@admin.register(BadgeAccessLog)
class BadgeAccessLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'card', 'status', 'badgeaccess', 'request_ip', )
