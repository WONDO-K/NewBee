# Generated by Django 4.2.8 on 2024-05-17 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_depositproduct_rename_option_bankoption_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depositproductoption',
            old_name='DepositProduct',
            new_name='depoist_product',
        ),
    ]