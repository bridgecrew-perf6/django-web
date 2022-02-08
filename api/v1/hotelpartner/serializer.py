from rest_framework import serializers
from hotelpartner.models import HotelChain

class HotelChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelChain
        fields = "__all__"