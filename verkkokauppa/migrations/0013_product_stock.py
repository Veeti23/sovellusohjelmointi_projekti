# Generated by Django 5.1.4 on 2024-12-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verkkokauppa', '0012_alter_review_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0, help_text='Lisää tuotteen varastomäärä'),
        ),
    ]
