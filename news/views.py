from django.shortcuts import render
from fond.models import *
from news.models import *
from django.views.generic import View, ListView
from django.db.models import Q


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


class AllNews(ListView):
    """Вывод всех новостей"""

    model = News
    template_name = 'fond/news.html'
    queryset = News.objects.all()


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


class SearchView(View):
    """Поиск по сайту"""

    def post(self, request, *args, **kwargs):
        query = self.request.POST.get('q')
        founded = News.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        context = {'founded': founded}
        return render(request, 'fond/search.html', context)
