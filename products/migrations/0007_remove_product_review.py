# Generated by Django 4.0.6 on 2022-08-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_alchol_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
    ]
