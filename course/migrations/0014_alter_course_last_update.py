# Generated by Django 4.2.5 on 2023-10-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_course_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.TimeField(auto_now=True, null=True, verbose_name='последнее обновление'),
        ),
    ]