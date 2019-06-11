from sobstvenikam.views import *
from django.urls import path, include

urlpatterns = [
    path('sob/<slug:slug>/', SobstvenikamView.as_view(), name='sob'),
    path('recomend/', RecommendationView.as_view(), name='rec'),
    path('recomend/<slug:slug>/', ChoicesView.as_view(), name='one_rec')
]
