from django.conf import settings
from django.conf.urls.static import static
from fond.views import *
from django.urls import path, include

urlpatterns = [
                  path('o_fonde/', AllFond.as_view(), name='allfond'),
                  path('ceo/', CeoView.as_view(), name='ceo'),
                  path('aim/', AimView.as_view(), name='aim'),
                  path('contacts/', ContactView.as_view(), name='contacts'),
                  path('infograph/', InfographView.as_view(), name='infograph'),
                  path('<slug:slug>/', VcontrolView.as_view(), name='control')
              ]
