# Generated by Django 5.1.4 on 2024-12-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verkkokauppa', '0011_alter_product_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=300),
        ),
    ]