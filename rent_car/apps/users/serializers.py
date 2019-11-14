from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from django.contrib.auth.models import User
from apps.cars.serializers import CarCreateSerializer


class UserListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='user_detail_url', lookup_field='id')

    class Meta:
        model = User
        fields = ('id','username','first_name','email','url')


class UserDetailSerializer(ModelSerializer):
    cars = SerializerMethodField()

    class Meta:
        model = User
        fields = ('id','username','first_name','email', 'cars')

    def get_cars(self, obj):
        if obj.car_set.all():
            return CarCreateSerializer(obj.car_set.all(), many=True).data
        return None




class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','username','email','password')


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','username','email')