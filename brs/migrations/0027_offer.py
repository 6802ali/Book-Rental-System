# Generated by Django 4.2.2 on 2023-07-17 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0026_delete_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.IntegerField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='brs.book')),
            ],
        ),
    ]