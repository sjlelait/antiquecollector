# Generated by Django 4.1.7 on 2023-04-11 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_rename_admirers_admirer'),
    ]

    operations = [
        migrations.AddField(
            model_name='antique',
            name='admirers',
            field=models.ManyToManyField(to='main_app.admirer'),
        ),
    ]