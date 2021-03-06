# Generated by Django 3.1.4 on 2021-01-04 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210104_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
                ('product_brand', models.CharField(default='Not Specified', max_length=200, verbose_name='Product_Brand')),
                ('year_of_manufacture', models.IntegerField(null=True, verbose_name='Year_Of_Manufacture')),
                ('color', models.CharField(default='Not specified', max_length=50, verbose_name='Color')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('product_image', models.ImageField(default='No image available', upload_to='', verbose_name='Product_Image')),
                ('size', models.CharField(default='Small', max_length=100, verbose_name='Size')),
                ('weight', models.DecimalField(decimal_places=3, default='180.00', max_digits=12, verbose_name='Weight')),
                ('description', models.CharField(default='Not Specified', max_length=300, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Good',
                'verbose_name_plural': 'Goods',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Good')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
                'db_table': 'products_categories',
            },
        ),
    ]
