# Generated by Django 4.2.16 on 2025-02-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0070_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagehero',
            name='background_video_url',
            field=models.CharField(blank=True, help_text='mp4 video', max_length=1000, null=True, verbose_name='Background video'),
        ),
    ]
