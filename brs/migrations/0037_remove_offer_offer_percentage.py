# Generated by Django 4.2.2 on 2023-07-17 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0036_alter_offer_offer_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='offer_percentage',
        ),
    ]
