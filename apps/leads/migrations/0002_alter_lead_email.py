# Generated by Django 4.2.21 on 2025-05-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
