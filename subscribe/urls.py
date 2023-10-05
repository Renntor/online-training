from subscribe.apps import SubscribeConfig
from django.urls import path
from subscribe.views import SubscribeListAPIView

app_name = SubscribeConfig.name

urlpatterns = [
    path('', SubscribeListAPIView.as_view(), name='subscribe_list'),
]
