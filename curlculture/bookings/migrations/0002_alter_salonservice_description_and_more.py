# Generated by Django 4.2.19 on 2025-05-17 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salonservice',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='salonservice',
            name='duration',
            field=models.DurationField(),
        ),
    ]
