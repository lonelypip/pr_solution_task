from rest_framework.serializers import ModelSerializer
from .models import Car



class CarCreateSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('name','year')


class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('id','owner','name','year','date')
