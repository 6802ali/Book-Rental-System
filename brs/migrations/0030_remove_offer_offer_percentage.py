# Generated by Django 4.2.2 on 2023-07-17 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0029_offer_offer_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='offer_percentage',
        ),
    ]
