# Generated by Django 4.2.6 on 2023-11-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issued',
            field=models.BooleanField(default=False),
        ),
    ]
