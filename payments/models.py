from django.conf import settings
from django.db import models
from course.models import Course
from users.models import NULLABLE


class PaymentsCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, verbose_name='курс')

    payment_url = models.URLField(max_length=200, verbose_name='ссылка на оплату', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return self.payment_url

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
