# Generated by Django 3.2.9 on 2021-11-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_category',
            field=models.CharField(max_length=100),
        ),
    ]
