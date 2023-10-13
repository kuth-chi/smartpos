from django.urls import path
from . import views
import web.org_views

app_name ='web'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('change_language/<str:language_code>/', views.change_language, name='change_language'),
    path('accounts/dashboard/home/', views.user_profile, name='user_home'),
    path('dashboard/<str:uuid>/', views.dashboard_user, name='dashboard'),
    # Organization
    path('<str:uuid>/dashboard/', web.org_views.org_dashboard_view, name='org_dashboard'),
    
    # User Profile
    path('profiles/', views.profile_list, name='profile_list'),
    path('profile/<uuid:user_uuid>/', views.public_profile, name='pub_profile'),
    
    # QR Code    
    path('vcard/<uuid:user_uuid>/', views.generate_vcard_qr, name='generate_vcard_qr'),
]
