from django.urls import path
from .views import CarCreateView, CarListAPIView


urlpatterns = [
    path('', CarListAPIView.as_view(), name='car_list_url'),
    path('create/', CarCreateView.as_view(), name='car_create_url'),
]
