# Generated by Django 4.2.16 on 2025-01-01 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contactpage_body_alter_contactpage_bottom_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='hero_title',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='script_title',
        ),
    ]
