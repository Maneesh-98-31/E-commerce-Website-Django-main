# Generated by Django 3.2.9 on 2021-11-13 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]
