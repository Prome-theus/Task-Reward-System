# Generated by Django 2.2.18 on 2024-05-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0007_auto_20240503_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]