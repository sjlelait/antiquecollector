# Generated by Django 4.1.7 on 2023-04-10 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_cleaning_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cleaning',
            options={'ordering': ['-date']},
        ),
    ]
