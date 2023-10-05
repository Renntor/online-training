from rest_framework import generics
from subscribe.models import SubscribeUser
from subscribe.serializers import SubscribeSerializer


class SubscribeListAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = SubscribeUser.objects.all()