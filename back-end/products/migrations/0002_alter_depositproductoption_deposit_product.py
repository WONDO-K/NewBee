# Generated by Django 4.2.8 on 2024-05-17 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositproductoption',
            name='deposit_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='products.depositproduct'),
        ),
    ]