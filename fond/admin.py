from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent',)
    mptt_level_indent = 20


class CeoAdmin(MPTTModelAdmin):
    list_display = ('name', 'position',)


class AimAdmin(MPTTModelAdmin):
    list_display = ('id',)
    mptt_level_indent = 20


admin.site.register(Aim, AimAdmin)
admin.site.register(CategoryFond, CategoryAdmin)
admin.site.register(CeoFond, CeoAdmin)
