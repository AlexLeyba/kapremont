from django.contrib import admin
from django.contrib import admin
from .models import *


class FilesInstanceInlineSob(admin.TabularInline):
    model = FilesBarModel


@admin.register(Bargaining)
class ChoicesInstanceInlineBar(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [FilesInstanceInlineSob]
