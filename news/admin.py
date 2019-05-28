from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class InfoCoinAdmin(admin.ModelAdmin):
    list_display = ('all_coin', 'all_home', 'paid', 'repaired',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('url',)


admin.site.register(Partners, PartnersAdmin)
admin.site.register(InfoCoin, InfoCoinAdmin)
admin.site.register(News, NewsAdmin)
