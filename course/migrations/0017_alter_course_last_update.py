# Generated by Django 4.2.5 on 2023-10-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_alter_course_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='последнее обновление'),
        ),
    ]