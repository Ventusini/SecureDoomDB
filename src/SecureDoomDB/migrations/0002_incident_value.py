# Generated by Django 2.0.7 on 2018-08-01 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureDoomDB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='value',
            field=models.PositiveIntegerField(default=1),
        ),
    ]