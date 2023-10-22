from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Business)
admin.site.register(BusinessAddress)
admin.site.register(EstablishedDate)
admin.site.register(BranchAddress)
admin.site.register(Branch)