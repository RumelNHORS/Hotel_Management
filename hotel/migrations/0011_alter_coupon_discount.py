# Generated by Django 4.2 on 2024-08-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_alter_booking_successid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]
