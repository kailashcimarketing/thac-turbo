# Generated by Django 4.2.16 on 2025-05-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilityhire', '0026_alter_facilityhireformpage_bottom_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilityhireformpage',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
