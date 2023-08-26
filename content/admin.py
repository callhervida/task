from django.contrib import admin
from .models import Content, Rate


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_count', 'rate_mean')


admin.site.register(Content, ContentAdmin)
admin.site.register(Rate)
