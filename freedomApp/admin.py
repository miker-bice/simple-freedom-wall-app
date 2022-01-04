from django.contrib import admin
from .models import Confession, Comment


class ConfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_alias', 'confession', 'timestamp')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'commenter_name', 'comment_body', 'comment_timestamp', 'target')


# Register your models here.
admin.site.register(Confession, ConfessionAdmin)
admin.site.register(Comment, CommentAdmin)
