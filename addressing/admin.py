from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(CountryLeader)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Commune)
admin.site.register(Village)