# Generated by Django 4.0.6 on 2022-08-01 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
            ],
            options={
                'db_table': 'al_categories',
            },
        ),
        migrations.CreateModel(
            name='MbCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
            ],
            options={
                'db_table': 'mb_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('scent', models.CharField(max_length=50, null=True)),
                ('alchol_level', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True)),
                ('al_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.alcategory')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=150)),
            ],
            options={
                'db_table': 'products_images',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.tag')),
            ],
            options={
                'db_table': 'products_tags',
            },
        ),
        migrations.CreateModel(
            name='ProductProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productimage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'products_products_images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(through='products.ProductProductImage', to='products.productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='mb_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.mbcategory'),
        ),
    ]
