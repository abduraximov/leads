# Generated by Django 4.2.21 on 2025-05-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('super_admin', 'Super Admin'), ('attorney', 'Attorney'), ('client', 'Client')], max_length=50, null=True, verbose_name='Role'),
        ),
    ]
