# Generated by Django 4.2.5 on 2023-11-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='is_profcom',
            field=models.BooleanField(default=True),
        ),
    ]
