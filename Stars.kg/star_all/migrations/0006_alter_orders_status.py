# Generated by Django 4.1 on 2023-01-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_all', '0005_orders_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(default='Новый', max_length=200),
        ),
    ]