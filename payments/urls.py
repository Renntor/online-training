from payments.apps import PaymentsConfig
from django.urls import path
from payments.views import PaymentsCourseCreateAPIView, PaymentsCourseListAPIView

app_name = PaymentsConfig.name

urlpatterns = [
    path('', PaymentsCourseListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentsCourseCreateAPIView.as_view(), name='payment_create'),
]
