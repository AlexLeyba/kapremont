from itertools import chain
from django.shortcuts import render
from fond.models import *
from news.models import *
from bargaining.models import *
from reports.models import *
from sobstvenikam.models import *
from django.views.generic import View, ListView
from django.db.models import Q
from fond.models import ArticleManager


class General(View):
    """Главная страница"""

    @staticmethod
    def get(request):
        try:
            las = News.objects.order_by('id').last()
            last_three = News.objects.order_by('-id')[0:3]
            coin = InfoCoin.objects.all()
            partners = Partners.objects.all()
            context = {
                'partners': partners,
                'last': las,
                'last_three': last_three,
                'info': coin,
            }
            return render(request, 'fond/general.html', context)
        except:
            partners = Partners.objects.all()
            coin = InfoCoin.objects.all()
            context = {
                'partners': partners,
                'info': coin,

            }
            return render(request, 'fond/general.html', context)


class SearchView(View):
    """Поиск по всему сайту"""

    def post(self, request, *args, **kwargs):
        q = request.POST.get("q")
        if q:
            query_sets = []
            query_sets.append(CeoFond.objects.search(query=q))
            query_sets.append(News.objects.search(query=q))
            query_sets.append(Vcontrol.objects.search(query=q))
            query_sets.append(FilesModel.objects.search(query=q))

            query_sets.append(Bargaining.objects.search(query=q))
            query_sets.append(FilesBarModel.objects.search(query=q))

            query_sets.append(ReportModel.objects.search(query=q))
            query_sets.append(FilesReports.objects.search(query=q))

            query_sets.append(Sobstvenikam.objects.search(query=q))
            query_sets.append(RecommendationsSob.objects.search(query=q))
            query_sets.append(FilesSobModel.objects.search(query=q))

            final_set = list(chain(*query_sets))
            final_set.sort(key=lambda x: x.name, reverse=True)
            context = {
                'found': query_sets
            }
        return render(request, 'fond/search.html', context)


class AllNews(View):
    """Вывод всех новостей"""

    def get(self, request):
        news = News.objects.order_by('id')[::-1]
        context = {
            'news': news
        }
        return render(request, 'fond/news.html', context)


class SingleNews(View):
    """Вывод полной статьи при нажатии на привью"""

    @staticmethod
    def get(request, pk):
        single = News.objects.get(id=pk)
        last_six = News.objects.order_by('-id')[0:6]
        context = {
            'single': single,
            'last_six': last_six
        }
        return render(request, 'fond/single.html', context)


class SortNews(View):
    def post(self, request):
        form = request.POST.get('calendar')
        calendar = News.objects.filter(date=form)
        context = {
            'calendar': calendar
        }
        return render(request, 'fond/sortnews.html', context)
