# Generated by Django 4.1.7 on 2023-04-10 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_cleaning_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admirers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
