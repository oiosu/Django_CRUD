# Generated by Django 3.2.13 on 2024-01-16 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20240116_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
