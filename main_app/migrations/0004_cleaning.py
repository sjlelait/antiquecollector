# Generated by Django 4.1.7 on 2023-04-10 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_antique_description_alter_antique_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('D', 'Dust'), ('P', 'Polish'), ('C', 'Cleaning')], default='D', max_length=1, verbose_name='cleaning type')),
                ('antique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.antique')),
            ],
        ),
    ]
