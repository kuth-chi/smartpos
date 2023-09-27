from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('change_language/<str:language_code>/', views.change_language, name='change_language'),
]
