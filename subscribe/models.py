from django.db import models
from course.models import Course
from users.models import User, NULLABLE


class SubscribeUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')

    subscribe = models.BooleanField(default=False, verbose_name='активная подписка')

    def __str__(self):
        return self.subscribe

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
