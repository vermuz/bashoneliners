from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models

from oneliners.models import HackerProfile, OneLiner
from social_django.models import UserSocialAuth


class UserSocialAuthInline(admin.StackedInline):
    model = UserSocialAuth
    show_change_link = True


class UserAdmin(admin.ModelAdmin):
    list_display = ('oneliner_count', 'last_login', 'id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username',)
    inlines = (UserSocialAuthInline,)

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('oneliner'))
        qs = qs.order_by('-oneliner__count')
        return qs

    def oneliner_count(self, obj):
        return obj.oneliner__count

    oneliner_count.admin_order_field = 'oneliner_count'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class OneLinerAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_published', 'was_tweeted', 'summary', 'created_dt',)


class HackerProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'get_date_joined', 'display_name', 'twitter_name',)


admin.site.register(OneLiner, OneLinerAdmin)
admin.site.register(HackerProfile, HackerProfileAdmin)
