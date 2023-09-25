from django.shortcuts import render
from rest_framework import viewsets
from users.seriliazers import UserSerializer
from users.models import User


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
