# Generated by Django 4.1.7 on 2023-04-10 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_admirers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admirers',
            new_name='Admirer',
        ),
    ]