"""
URL configuration for gettingstarted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from .settings import IS_HEROKU_APP



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls', namespace="accounts_app")),
    path('', include('web.urls', namespace="web_app")),
    path('', include('organizations.urls', namespace="org_app")),
    path('', include('addressing.urls', namespace="addressing_app")),   
]

urlpatterns += i18n_patterns(

    re_path('', include('accounts.urls', 'accounts')),
    re_path('', include('web.urls', 'web')),
    re_path('', include('organizations.urls', 'organizations')),
    re_path('', include('addressing.urls', 'addressing')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
    
if not IS_HEROKU_APP:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
    

