from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DistrictViewSet, ProvinceViewSet, CommuneViewSet
from . import views


app_name = 'addressing'
router = DefaultRouter()
router.register(r'communes', CommuneViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'provinces', ProvinceViewSet)
urlpatterns = [
    path('geography/', views.GeoIndexView, name='geography'),
    path('geography/countries/', views.country_list, name='countries'),
    # Province
    path('geography/provinces/', views.province_list, name='provinces'),
    path('geography/provinces/<int:pk>/', views.province_detail, name='province_detail'),
    # District
    path('geography/districts/', views.district_list, name='districts'),
    # Commune
    path('geography/communes/', views.commune_list, name='communes'),
    # API
    path('api/v1/geography/', include(router.urls)),
]
