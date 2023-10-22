from rest_framework import serializers
from addressing.serializers import CountrySerializer, ProvinceSerializer, DistrictSerializer, CommuneSerializer, VillageSerializer
from .models import UserAddress, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
class UserAddressSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    country = CountrySerializer()
    state = ProvinceSerializer()
    city = DistrictSerializer()
    commune = CommuneSerializer()
    village = VillageSerializer()
    class Meta:
        model = UserAddress
        fields = '__all__'