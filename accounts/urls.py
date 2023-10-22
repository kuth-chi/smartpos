from django.urls import path
from . import views
from .views import UserAddressCreateView, UserAddressRetrieveView, UserAddressUpdateView, UserAddressDeleteView, UserAddressListView

# URLS
app_name="accounts"
urlpatterns = [
        
        path('accounts/login/', views.user_login, name='login'),
        path('accounts/logout/', views.logout_user, name='logout_user'),
        path('accounts/signup/', views.user_signup, name='signup'),
        path('accounts/my-account/', views.user_profile, name='profile'),
        path('accounts/<uuid:user_uuid>/information/', views.user_info_view, name='user_info'),
        # Address
        path('<uuid:user_uuid>/addresses/', views.user_address_list, name='user_address_list'),
        path('<uuid:user_uuid>/address/create/', views.create_user_address, name='create_user_address'),
        # API
        path('api/v1/user/addresses/', UserAddressCreateView.as_view(), name='user_address_create_api'),
        path('api/v1/user/addresses/list/', UserAddressListView.as_view(), name='user_address_list_api'),
        path('api/v1/user/addresses/<int:pk>/', UserAddressRetrieveView.as_view(), name='user_address_detail_api'),
        path('api/v1/user/addresses/<int:pk>/update/', UserAddressUpdateView.as_view(), name='user_address_update_api'),
        path('api/v1/user/addresses/<int:pk>/delete/', UserAddressDeleteView.as_view(), name='user_address_delete_api'),
]
