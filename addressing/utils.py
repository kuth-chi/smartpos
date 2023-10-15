from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from .models import Province, District, Commune

def count_provinces_by_country_and_date(country_id, start_date, end_date):
    provinces = Province.objects.filter(
        country_id=country_id,
        timestamp__gte=start_date,
        timestamp__lte=end_date
    )
    return provinces.count()

def count_districts_by_province_and_date(province_id, start_date, end_date):
    districts = District.objects.filter(
        province_id=province_id,
        timestamp__gte=start_date,
        timestamp__lte=end_date
    )
    return districts.count()

def count_communes_by_district_and_date(district, start_date, end_date):
    communes = District.objects.filter(
        district = district,
        timestamp__gte=start_date,
        timestamp__lte=end_date
    )
    return communes.count()

def count_villages_by_district_and_date(commune, start_date, end_date):
    villages = District.objects.filter(
        commune=commune,
        timestamp__gte=start_date,
        timestamp__lte=end_date
    )
    return villages.count()


def provinces_in_country(country_id):
    try:
        provinces = Province.objects.filter(country_id=country_id)
        return provinces.count()
    except ObjectDoesNotExist:
        return 0
    
    
def count_districts_by_province(province_id):
    try:
        districts = District.objects.filter(province_id=province_id)
        return districts.count()
    except ObjectDoesNotExist:
        return 0
    
def communes_by_district(district_id):
    try:
        communes = Commune.objects.filter(district_id=district_id)
        return communes.count()
    except ObjectDoesNotExist:
        return 0

