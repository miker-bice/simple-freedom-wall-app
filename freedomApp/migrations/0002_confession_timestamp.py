# Generated by Django 4.0 on 2021-12-13 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freedomApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confession',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
