from django.shortcuts import render
from fond.models import *
from news.models import *
from django.views.generic import View, ListView
from django.db.models import Q

# Раздел меню О фонде

class VcontrolView(View):
    def get(self, request, slug):
        control = Vcontrol.objects.filter(slug=slug)
        context = {
            'control': control
        }
        return render(request, 'fond/vkontrol.html', context)


class InfographView(View):
    """Инфографика"""

    def get(self, request):
        info = Infograph.objects.all()
        context = {
            'info': info
        }
        return render(request, 'fond/infografics.html', context)


class CeoView(View):
    """Руководители фонда"""

    @staticmethod
    def get(request):
        ceo = CeoFond.objects.all()
        context = {
            'ceo': ceo
        }
        return render(request, 'fond/ceo.html', context)


class AimView(View):
    """Цели и функции"""

    def get(self, request):
        aim = Aim.objects.all()
        context = {
            'aim': aim
        }
        return render(request, 'fond/aim.html', context)


class ContactView(View):
    """ Контакты """

    def get(self, requset):
        return render(requset, 'fond/contacts.html')


class AllFond(View):
    """Все подкатегории в О фонде"""

    def get(self, request):
        return render(request, 'fond/allfond.html')
