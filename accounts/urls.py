from django.urls import path
from . import views

# URLS
urlpatterns = [
        path('accounts/dashboard/', views.dashboard_user, name='dashboard'),
        path('accounts/login/', views.user_login, name='user_login'),
        path('accounts/logout/', views.logout_user, name='logout_user'),
        path('accounts/signup/', views.user_signup, name='user_signup'),


]
