# Generated by Django 3.1.4 on 2022-02-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_order_orderitem_review_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='trainer',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='name',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
