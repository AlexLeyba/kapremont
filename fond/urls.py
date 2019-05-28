from django.conf import settings
from django.conf.urls.static import static
from fond.views import *
from django.urls import path, include

urlpatterns = [
                  path('ceo/', CeoView.as_view(), name='ceo'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
