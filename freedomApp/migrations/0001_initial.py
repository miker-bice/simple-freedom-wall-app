# Generated by Django 4.0 on 2021-12-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_alias', models.CharField(max_length=15)),
                ('confession', models.CharField(max_length=2000)),
            ],
        ),
    ]
