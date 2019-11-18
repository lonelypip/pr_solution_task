from django.urls import path
from .views import CarCreateView, CarListAPIView, OrderCreateView, OrderCommentView


urlpatterns = [
    path('', CarListAPIView.as_view(), name='car_list_url'),
    path('create/', CarCreateView.as_view(), name='car_create_url'),
    path('order/', OrderCommentView.as_view(), name='order_create_url'),
]
