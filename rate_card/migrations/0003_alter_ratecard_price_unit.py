# Generated by Django 5.1.7 on 2025-04-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_card', '0002_ratecard_include_rate_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratecard',
            name='price_unit',
            field=models.CharField(choices=[('hour', 'Hour'), ('humanday', 'Human Day'), ('monthly', 'Monthly'), ('onetime', 'One Time')], default='onetime', max_length=100),
        ),
    ]
