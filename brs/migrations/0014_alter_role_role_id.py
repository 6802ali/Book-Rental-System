# Generated by Django 4.2.2 on 2023-07-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0013_alter_role_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
