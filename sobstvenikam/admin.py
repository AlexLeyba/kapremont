from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class FilesInstanceInlineSob(admin.TabularInline):
    model = FilesSobModel


@admin.register(Choices)
class ChoicesInstanceInlineSob(admin.ModelAdmin):
    inlines = [FilesInstanceInlineSob]


@admin.register(Sobstvenikam)
class SoblAdmin(MPTTModelAdmin):
    list_display = ('name', 'text',)
    inlines = [FilesInstanceInlineSob]


@admin.register(RecommendationsSob)
class RecommendationsSobAdmin(admin.ModelAdmin):
    list_display = ('name',)