from django.shortcuts import render
from django.views.generic.base import View
from sobstvenikam.models import *


class SobstvenikamView(View):
    def get(self, request, slug):
        sob = Sobstvenikam.objects.filter(slug=slug)
        context = {
            'sob': sob
        }
        return render(request, 'sobstvenikam/sob.html', context)


class RecommendationView(View):
    def get(self, request):
        name = RecommendationsSob.objects.all()
        choices = Choices.objects.all()
        context = {
            'name': name,
            'choices': choices,

        }
        return render(request, 'sobstvenikam/recomend.html', context)


class ChoicesView(View):
    def get(self, requset, slug):
        name = RecommendationsSob.objects.all()
        choices = Choices.objects.all()
        one_choice = Choices.objects.filter(slug=slug)
        context = {
            'vkladka': one_choice,
            'name': name,
            'choices': choices,

        }
        return render(requset, 'sobstvenikam/onerecomend.html', context )
