from datetime import datetime, timedelta
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from accounts.models import UserAddress
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator
# DRF
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Country, Province, District, Commune, Village
from .utils import *
from .serializers import *
# Create your views here.


def country_list(request):
    try:
        # Retrieve the latest country entry
        # Replace 'created_at' with the actual field you want to use for ordering
        latest_country = Country.objects.order_by('-timestamp').first()
        countries = Country.objects.all()
        count_countries = countries.count()
    except Country.DoesNotExist:
        latest_country = None
        countries = None
        count_countries = 0

    context = {
        'title_page': _('Countries'),
        'header_title': _('Countries'),
        'countries': countries,
        'total_countries': count_countries,
        'latest_country': latest_country,  # Add the latest_country to the context
    }
    return render(request, 'addressing/countries/list.html', context)

def province_list(request):
    current_domain = request.get_host()
    api_url = f"{request.scheme}://{current_domain}/api/v1/geography/provinces/"
    province_per_page = int(request.GET.get('province_per_page', 10))
    try:
        provinces = Province.objects.annotate(districts=Count('district')).order_by('-timestamp')
        # Create a Paginator instance and specify the number of items per page
        paginator = Paginator(provinces, province_per_page)
        page = request.GET.get('page')

        provinces = paginator.get_page(page)
    except Province.DoesNotExist:
        provinces = None
        
        
    context = {
        'title_page': _('Provinces'),
        'header_title': _('Provinces'),
        'api_url': api_url,
        'provinces': provinces,
        'count_districts_by_province': count_districts_by_province,
        'items_per_page': province_per_page,
        
        
    }
    return render(request, 'addressing/provinces/list.html', context)
# Province API
class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data

        # Annotate the number of districts for each province and add it to serialized data
        for province_data in serialized_data:
            try:
                province_id = province_data['id']
                district_count = District.objects.filter(province_id=province_id).count()
                province_data['districts'] = district_count
            except KeyError:
                # Handle the case where 'id' is not present in the dictionary
                province_data['districts'] = 0  # or another default value

        return Response(serialized_data)
    


# District
def district_list(request):
    district_per_page = int(request.GET.get('district_per_page', 10))
    try:
        districts = District.objects.annotate(communes=Count('commune')).order_by('-timestamp')
        # Create a Paginator instance and specify the number of items per page
        paginator = Paginator(districts, district_per_page)
        page = request.GET.get('page')

        districts = paginator.get_page(page)
    except District.DoesNotExist:
        districts = None
        
        
    context = {
        'title_page': _('Districts'),
        'header_title': _('Districts'),
        'districts': districts,
        'communes_by_district': communes_by_district,
        'items_per_page': district_per_page,
        
    }
    return render(request, 'addressing/districts/list.html', context)
# District API
class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data

        # Annotate the number of communes for each district and add it to serialized data
        for district_data in serialized_data:
            try:
                district_id = district_data['id']
                commune_count = Commune.objects.filter(district_id=district_id).count()
                district_data['communes'] = commune_count
            except KeyError:
                # Handle the case where 'id' is not present in the dictionary
                district_data['communes'] = 0  # or another default value

        return Response(serialized_data)



def GeoIndexView(request):
    # Calculate the start and end dates for the last 28 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=28)
    start_before_28_days = start_date - timedelta(days=28)
    
    
    # Country Block
    count_user_addresses_in_random_district = 0
    
    try:
        countries = Country.objects.all()
        total_countries = countries.count()
        random_one_country = countries.order_by('?').first()
        if random_one_country:
            country_id = random_one_country.id 
        else:
            country_id = None    
        count_provinces_by_country = provinces_in_country(country_id)
        
        count_address_in_country = {}
        for country in countries:
            count_address_in_country[country.name] = UserAddress.objects.filter(country=country).count()
        total_address_count = sum(count_address_in_country.values())
        province_count_by_country_with_date = count_provinces_by_country_and_date(country_id, start_date, end_date)
    except Country.DoesNotExist:
        countries = None
        total_countries = 0
        total_address_count = 0
        province_count_by_country_with_date = 0
        random_one_country = 0
    latest_country = Country.objects.order_by('-timestamp').first()
    
    # Provinces
    try:
        provinces = Province.objects.all()
        total_provinces = provinces.count()
        random_province = provinces.order_by('?').first()
        if random_province:
            province_id = random_province.id
        else:
            province_id = None
        # Count District in Random Provinces
        count_districts_in_province = count_districts_by_province(province_id)
        
        # Count address in last 28 day
        count_address_28_days_before_last_28_days = UserAddress.objects.filter(
            state=province_id,
            created_date__gte=start_before_28_days,
            created_date__lte=start_date
        ).count()
        count_address_last_28_days = UserAddress.objects.filter(
            state = province_id,
            created_date__gte=start_date,
            created_date__lte=end_date
        ).count()
        
        count_address_in_province = {}
        for province in provinces:
            count_address_in_province[province.name] = UserAddress.objects.filter(state=province).count()
        total_address_count_in_province = sum(count_address_in_province.values())
        
        count_user_addresses_in_random_province = UserAddress.objects.filter(state=province_id).count()
        address_count_in_province_by_date = count_districts_by_province_and_date(province_id, start_date, end_date)
        
    except Province.DoesNotExist:
        provinces = None
        random_province = None
        total_provinces = 0
        count_address_last_28_days = 0
        count_user_addresses_in_random_province = 0
        count_address_28_days_before_last_28_days = 0
        
    latest_province = Province.objects.order_by('-timestamp').first()
    
    try:
        districts = District.objects.all()
        total_districts = districts.count()
        
        if districts:
            random_district = districts.order_by('?').first()
            if random_district:
                district_id = random_district.id
            else:
                district_id = None
            try:
                # Count address in last 28 day
                count_address_28_days_before_last_28_days = UserAddress.objects.filter(
                        city=district_id,
                        created_date__gte=start_before_28_days,
                        created_date__lte=start_date
                ).count()
                count_user_addresses_in_random_district = UserAddress.objects.filter(city=district_id).count()
                # all addresses in each district
                count_user_addresses_in_district = {}
                for district in  districts:
                    count_user_addresses_in_district[district.name] = UserAddress.objects.filter(city=district_id).count()
                total_address_in_district = sum(count_user_addresses_in_district.values())
                count_address_last_28_days = UserAddress.objects.filter(
                    city=district_id,
                    created_date__gte=start_date,
                    created_date__lte=end_date
                ).count()
            except UserAddress.DoesNotExist:
                count_address_28_days_before_last_28_days = 0
                count_user_addresses_in_random_district = 0
                count_address_last_28_days = 0
    except District.DoesNotExist:
        districts = None
        total_districts = 0
        
    latest_district = District.objects.order_by('-timestamp').first()
    
        
        
            
    
    
    # Commune
    try:
        communes = Commune.objects.all()
        total_communes = communes.count()
        if communes:
            random_commune = communes.order_by('?').first()
            if random_commune:
                commune_id = random_commune.id
            else:
                commune_id = None
    except Commune.DoesNotExist:
        communes = None
        total_communes = 0
    latest_commune = Commune.objects.order_by('-timestamp').first()
    
    
    try:
        villages = Village.objects.all()
        total_villages = villages.count()
    except Village.DoesNotExist:
        villages = None
        total_villages = 0
    latest_village = Village.objects.order_by('-timestamp').first()
    
    try:
        count_user_address = UserAddress.objects.all().count()
    except UserAddress.DoesNotExist:
        count_user_address = 0

    context = {
        'title_page': _('Address Management'),
        'header_title': _('Address Management'),
        'countries': countries,
        'total_countries': total_countries,
        'latest_country': latest_country,
        'provinces': provinces,
        'total_provinces': total_provinces,
        'latest_province': latest_province,
        'districts': districts,
        'total_districts': total_districts,
        'latest_district': latest_district,
        'Communes': communes,
        'total_communes': total_communes,
        'latest_commune': latest_commune,
        'Villages': villages,
        'total_villages': total_villages,
        'latest_village': latest_village,
        'count_user_address': total_address_count,
        'count_user_addresses_in_random_province': count_user_addresses_in_random_province,
        'random_province': random_province,
        'count_address_last_28_days': count_address_last_28_days,
        'count_address_28_days_before_last_28_days': count_address_28_days_before_last_28_days,
        'province_count_by_country_with_date': province_count_by_country_with_date,
        'count_provinces_by_country': count_provinces_by_country,
        'random_one_country': random_one_country,
        'count_user_addresses_in_random_district': count_user_addresses_in_random_district,
        'total_address_in_district': total_address_in_district,
        'address_count_in_province_by_date': address_count_in_province_by_date,
        'total_address_count_in_province': total_address_count_in_province,
        # District Block
        'count_districts_in_province': count_districts_in_province,
        'random_district': random_district,
        
    }
    return render(request, 'addressing/index.html', context)
