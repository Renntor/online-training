# Generated by Django 4.2.5 on 2023-11-07 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_course_price_lesson_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 7, 10, 38, 11, 752009, tzinfo=datetime.timezone.utc), null=True, verbose_name='последнее обновление'),
        ),
    ]
