from django.contrib import admin
from .models import Confession


class confessionAdmin(admin.ModelAdmin):
    list_display = ('user_alias', 'confession', 'timestamp')


# Register your models here.
admin.site.register(Confession, confessionAdmin)