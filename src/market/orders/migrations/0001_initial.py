# Generated by Django 3.2.22 on 2024-01-12 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sellers', '0008_auto_20240111_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='название')),
            ],
            options={
                'verbose_name': 'статус заказа',
                'verbose_name_plural': 'статусы заказа',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='общая стоимость заказа')),
                ('delivery_city', models.CharField(max_length=256, null=True, verbose_name='город заказчика')),
                ('delivery_address', models.TextField(verbose_name='адрес заказчика')),
                ('delivery_method', models.CharField(max_length=256, null=True, verbose_name='способ доставки')),
                ('payment_method', models.CharField(max_length=256, null=True, verbose_name='способ оплаты')),
                ('full_name', models.CharField(max_length=256, null=True, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=256, null=True, verbose_name='телефон')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='почта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время обновления заказа')),
                ('seller_products', models.ManyToManyField(related_name='orders', to='sellers.SellerProduct', verbose_name='продукты продавца')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.orderstatus', verbose_name='статус заказа')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
    ]
