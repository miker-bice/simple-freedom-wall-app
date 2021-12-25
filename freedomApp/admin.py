from django.contrib import admin
from .models import Confession, Comment


class confessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_alias', 'confession', 'timestamp')


class commentAdmin(admin.ModelAdmin):
    list_display = ('id', 'commenter_name','comment_body', 'comment_timestamp', 'target')


# Register your models here.
admin.site.register(Confession, confessionAdmin)
admin.site.register(Comment, commentAdmin)