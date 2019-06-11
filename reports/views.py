from django.shortcuts import render
from django.views.generic.base import View
from reports.models import *


class ReportView(View):
    def get(self, request, **kwargs):
        name = ReportModel.objects.filter(slug=kwargs.get("report"))
        choices = Reportchoice.objects.filter(rec=name.first())
        if kwargs.get("slug") is not None:
            one_choice = Reportchoice.objects.filter(slug=kwargs.get("slug"))
            name = ReportModel.objects.filter(reportchoice__slug=kwargs.get("slug"))
            choices = Reportchoice.objects.filter(rec=name.first())
            context = {
                'name': name,
                'choices': choices,
                'vkladka': one_choice,

            }
        else:
            context = {
                'name': name,
                'choices': choices,

            }
        return render(request, 'reports/one_report.html', context)
