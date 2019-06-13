from django.shortcuts import render
from django.views.generic.base import View
from bargaining.models import *


class BargainingView(View):
    def get(self, request, slug):
        bar = Bargaining.objects.filter(slug=slug)
        context = {
            'bar': bar
        }
        return render(request, 'bargaining/bargaining.html', context)


class SberProcedures(View):
    def get(self, request):
        return render(request, 'bargaining/sberprocedures.html')


class SberContracts(View):
    def get(self, request):
        return render(request, 'bargaining/sbercontracts.html')


class Purchases(View):
    def get(self, request):
        return render(request, 'bargaining/purchases.html')


class Registry(View):
    def get(self, request):
        return render(request, 'bargaining/registry.html')
