# Generated by Django 4.2.16 on 2024-11-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tuotteet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=100)),
                ('hinta', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kuvaus', models.TextField()),
            ],
        ),
    ]
