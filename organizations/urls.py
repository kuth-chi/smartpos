from django.urls import path
from . import views

app_name = 'organizations'
urlpatterns = [
    path('<int:pk>/organization/', views.OrganizationIndexView, name='organizations_index'),
]
