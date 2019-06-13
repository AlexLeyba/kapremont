from bargaining.views import *
from django.urls import path, include

urlpatterns = [
    path('sberprocedures/', SberProcedures.as_view(), name='procedures'),
    path('sbercontracts/', SberContracts.as_view(), name='contracts'),
    path('purchases/', Purchases.as_view(), name='purchases'),
    path('registry/', SberProcedures.as_view(), name='registry'),
    path('bar/<slug:slug>/', BargainingView.as_view(), name='bar')

]
