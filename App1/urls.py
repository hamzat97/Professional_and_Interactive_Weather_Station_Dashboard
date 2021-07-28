from django.urls import path
from . import views

urlpatterns = [
  path('', views.Index),
  path('today', views.Today),
  path('yesterday', views.Yesterday),
  path('lastweek', views.LastWeek),
  path('lastmonth', views.LastMonth),
  path('alltime', views.AllTime), 
  path('custom', views.Custom),
  path('download', views.DownloadLDA),
  path('downloadtoday', views.DownloadToday),
  path('downloadyesterday', views.DownloadYesterday),
  path('downloadlastweek', views.DownloadLastWeek),
  path('downloadlastmonth', views.DownloadLastMonth),
  path('downloadalltime', views.DownloadAllTime),
  path('downloadcustom', views.DownloadCD)
]