from django.conf import settings
from django.conf.urls.static import static
from news.views import *
from django.urls import path, include

urlpatterns = [
                  path('', General.as_view()),
                  path('single/<int:pk>/', SingleNews.as_view(), name='single'),
                  path('search/', SearchView.as_view(), name='search'),
                  path('news/', AllNews.as_view(), name='news'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
