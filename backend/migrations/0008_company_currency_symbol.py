# Generated by Django 4.1 on 2024-03-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_reviews_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='currency_symbol',
            field=models.TextField(blank=True),
        ),
    ]