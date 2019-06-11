from news.views import *
from django.urls import path, include

urlpatterns = [
    path('', General.as_view()),
    path('news/', AllNews.as_view(), name='news'),
    path('single/<int:pk>/', SingleNews.as_view(), name='single'),
    path('search/', SearchView.as_view(), name='search'),
    path('sort/', SortNews.as_view(), name='sort')
]
