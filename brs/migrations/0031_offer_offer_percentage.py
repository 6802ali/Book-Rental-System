# Generated by Django 4.2.2 on 2023-07-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0030_remove_offer_offer_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]