from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class FilesInstanceInline(admin.TabularInline):
    model = FilesModel


@admin.register(Vcontrol)
class ControlAdmin(MPTTModelAdmin):
    list_display = ('name', 'text',)
    inlines = [FilesInstanceInline]


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent',)
    mptt_level_indent = 20


class CeoAdmin(admin.ModelAdmin):
    list_display = ('name', 'position',)


class AimAdmin(admin.ModelAdmin):
    list_display = ('id',)
    mptt_level_indent = 20


class InfographAdmn(admin.ModelAdmin):
    list_display = ('name', 'image', 'file')


admin.site.register(Infograph, InfographAdmn)
admin.site.register(Aim, AimAdmin)
admin.site.register(CategoryFond, CategoryAdmin)
admin.site.register(CeoFond, CeoAdmin)
