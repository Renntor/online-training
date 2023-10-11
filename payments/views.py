from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from course.models import Course
from payments.models import PaymentsCourse
from payments.serializer import PaymentsCourseSerializer
from payments.service import create_payment


# Create your views here.


class PaymentsCourseCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsCourseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pk = request.data['course']
        course = Course.objects.filter(pk=pk).first()
        request.data['payment_url'] = create_payment(course.title, course.price)
        data = super().post(request, *args, **kwargs)
        return data


class PaymentsCourseListAPIView(generics.ListAPIView):
    serializer_class = PaymentsCourseSerializer
    queryset = PaymentsCourse.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
