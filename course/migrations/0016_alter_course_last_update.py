# Generated by Django 4.2.5 on 2023-10-13 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_alter_course_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 13, 12, 9, 38, 583787), null=True, verbose_name='последнее обновление'),
        ),
    ]
