# Generated by Django 3.2.9 on 2021-11-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.TextField(max_length=30),
        ),
    ]
