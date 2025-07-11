# Generated by Django 4.2.16 on 2025-01-13 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('events', '0002_events_time_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text='Detail page hero image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
