# Generated by Django 4.1 on 2024-03-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_contact_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
