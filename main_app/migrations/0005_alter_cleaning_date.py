# Generated by Django 4.1.7 on 2023-04-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cleaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning',
            name='date',
            field=models.DateField(verbose_name='cleaning date'),
        ),
    ]
