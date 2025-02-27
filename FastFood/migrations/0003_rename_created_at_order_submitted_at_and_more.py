# Generated by Django 5.1.3 on 2025-01-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FastFood', '0002_alter_order_customer_name_alter_order_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='submitted_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='order_details',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(max_length=15),
        ),
    ]
