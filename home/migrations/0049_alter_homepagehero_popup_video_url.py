# Generated by Django 4.2.16 on 2025-01-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_alter_homepagehero_background_video_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagehero',
            name='popup_video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
