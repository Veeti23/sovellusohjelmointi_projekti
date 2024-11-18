# Generated by Django 4.2.16 on 2024-10-16 21:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crazy_book_clubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_modifield',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(help_text='Name of the person reviewing the book', max_length=100)),
                ('my_review', models.TextField()),
                ('stars', models.IntegerField(help_text='Rating of the book (0-5)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('unfinished', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(help_text='The book being reviewed', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='crazy_book_clubs.book')),
            ],
        ),
    ]