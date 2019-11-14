from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Car
from .serializers import CarCreateSerializer, CarListSerializer


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