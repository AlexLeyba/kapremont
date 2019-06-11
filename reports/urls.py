from reports.views import *
from django.urls import path, include

urlpatterns = [
    path('all-reports/<slug:report>/', ReportView.as_view(), name='report'),
    path('<slug:slug>/', ReportView.as_view(), name='one_report')
]
