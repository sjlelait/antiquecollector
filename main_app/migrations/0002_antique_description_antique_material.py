# Generated by Django 4.1.7 on 2023-04-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='antique',
            name='description',
            field=models.TextField(max_length=250, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='antique',
            name='material',
            field=models.CharField(max_length=75, null=True),
            preserve_default=False,
        ),
    ]
