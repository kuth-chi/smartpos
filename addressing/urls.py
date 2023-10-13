from django.urls import path
from . import views

app_name = 'addressing'
urlpatterns = [
    path('geography/', views.GeoIndexView, name='geography'),
    path('geography/countries/', views.country_list, name='countries'),
    # Province
    path('geography/provinces/', views.province_list, name='provinces'),
]
