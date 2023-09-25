from django.db import models
from users.models import NULLABLE


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(max_length=200, verbose_name='ссылка на видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
