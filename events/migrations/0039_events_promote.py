# Generated by Django 4.2.16 on 2025-06-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0038_events_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='promote',
            field=models.BooleanField(default=False, verbose_name='Promote'),
        ),
    ]
