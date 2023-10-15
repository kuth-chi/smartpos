from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DistrictViewSet, ProvinceViewSet
from . import views


app_name = 'addressing'
router = DefaultRouter()
router.register(r'districts', DistrictViewSet)
router.register(r'provinces', ProvinceViewSet)
urlpatterns = [
    path('geography/', views.GeoIndexView, name='geography'),
    path('geography/countries/', views.country_list, name='countries'),
    # Province
    path('geography/provinces/', views.province_list, name='provinces'),
    # District
    path('geography/districts/', views.district_list, name='districts'),
    # API
    path('api/v1/geography/', include(router.urls)),
]
