# Generated by Django 4.1.3 on 2022-11-22 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='isbn',
            field=models.IntegerField(default=13),
        ),
    ]
