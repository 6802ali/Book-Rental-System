# Generated by Django 4.2.2 on 2023-07-14 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0024_activity_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('book_type', models.CharField(max_length=50)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brs.author')),
            ],
        ),
    ]