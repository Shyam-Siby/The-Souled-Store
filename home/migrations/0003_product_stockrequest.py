# Generated by Django 5.0.2 on 2024-04-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_admin_login_supplier_product_stock_product_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stockrequest',
            field=models.BooleanField(default=False),
        ),
    ]