from django.urls import path
from . import views

# URLS
app_name="accounts"
urlpatterns = [
        
        path('accounts/login/', views.user_login, name='login'),
        path('accounts/logout/', views.logout_user, name='logout_user'),
        path('accounts/signup/', views.user_signup, name='signup'),
        path('accounts/my-account/', views.user_profile, name='profile'),
        # Address
        path('<uuid:user_uuid>/addresses/', views.user_address_list, name='user_address_list'),
        path('<uuid:user_uuid>/address/create/', views.create_user_address, name='create_user_address'),
]
