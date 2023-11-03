# Generated by Django 4.2.6 on 2023-10-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settingsapp', '0002_rename_cachetimes_cachetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachetime',
            name='banners_cache',
            field=models.IntegerField(default=600, verbose_name='Время кэширования Баннеров'),
        ),
        migrations.AlterField(
            model_name='cachetime',
            name='categories_cache',
            field=models.IntegerField(default=86400, verbose_name='Время кэширования Категорий товаров'),
        ),
        migrations.AlterField(
            model_name='cachetime',
            name='product_data_cache',
            field=models.IntegerField(default=86400, verbose_name='Время кэширования данных о Товаре'),
        ),
        migrations.AlterField(
            model_name='cachetime',
            name='products_cache',
            field=models.IntegerField(default=86400, verbose_name='Время кэширования списка Товаров из Каталога'),
        ),
        migrations.AlterField(
            model_name='cachetime',
            name='seller_data_cache',
            field=models.IntegerField(default=86400, verbose_name='Время кэширования данных о Продавце'),
        ),
        migrations.AlterField(
            model_name='cachetime',
            name='top_products_cache',
            field=models.IntegerField(default=86400, verbose_name='Время кэширования списка Топ-Товаров'),
        ),
    ]
