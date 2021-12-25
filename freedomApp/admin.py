from django.contrib import admin
from .models import Confession, Comment


class confessionAdmin(admin.ModelAdmin):
    list_display = ('user_alias', 'confession', 'timestamp')


class commentAdmin(admin.ModelAdmin):
    list_display = ('commenter_name', 'comment_timestamp')


# Register your models here.
admin.site.register(Confession, confessionAdmin)
admin.site.register(Comment, commentAdmin)