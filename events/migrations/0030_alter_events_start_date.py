# Generated by Django 4.2.16 on 2025-05-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0029_alter_events_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
