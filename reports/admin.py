from django.contrib import admin
from django.contrib import admin
from .models import *


class FilesInstanceInlineSob(admin.TabularInline):
    model = FilesReports


@admin.register(Reportchoice)
class ChoicesInstanceInlineSob(admin.ModelAdmin):
    inlines = [FilesInstanceInlineSob]


@admin.register(ReportModel)
class RecommendationsSobAdmin(admin.ModelAdmin):
    list_display = ('name',)
