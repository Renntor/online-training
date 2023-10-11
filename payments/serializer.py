from rest_framework import serializers

from payments.models import PaymentsCourse


class PaymentsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsCourse
        fields = ('course', 'payment_url',)
