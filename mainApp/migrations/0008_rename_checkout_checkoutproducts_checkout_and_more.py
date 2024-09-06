# Generated by Django 5.1 on 2024-09-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutproducts',
            old_name='Checkout',
            new_name='checkout',
        ),
        migrations.AddField(
            model_name='checkoutproducts',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='checkoutproducts',
            name='total',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
