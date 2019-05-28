from django.shortcuts import render
from fond.models import *
from news.models import *
from django.views.generic import View, ListView
from django.db.models import Q


class CeoView(View):
    """Руководители фонда"""

    @staticmethod
    def get(request,):
        ceo = CeoFond.objects.all()
        context = {
            'ceo': ceo
        }
        return render(request, 'fond/ceo.html', context)
