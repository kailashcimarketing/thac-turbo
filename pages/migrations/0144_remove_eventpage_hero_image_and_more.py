# Generated by Django 4.2.16 on 2025-05-19 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0143_eventpagehero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpage',
            name='hero_image',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='hero_script_title',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='hero_title',
        ),
    ]
