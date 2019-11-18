from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Car, Order
from .serializers import CarCreateSerializer, CarListSerializer, OrderCreateSerializer
from django.contrib.auth.models import User

class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    permission_classes = (IsAuthenticated,)


class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # send_mail(
        #     '',
        #     '',
        #     '',
        #     [self.request.user],
        # )
        serializer.save(owner=self.request.user)


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.POST.get('pk'):
            pk = request.POST.get('pk')
            try:
                car = Car.objects.get(pk=pk)
                order = Order.objects.create(car=car, user=request.user)
                serializer = OrderCreateSerializer(order, context={'request': request})
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            except:
                return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_403_FORBIDDEN)