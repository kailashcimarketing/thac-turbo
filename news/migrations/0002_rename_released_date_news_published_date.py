# Generated by Django 4.2.16 on 2024-10-07 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='released_date',
            new_name='published_date',
        ),
    ]
