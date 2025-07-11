# Generated by Django 4.2.16 on 2025-01-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_alter_formpage_bottom_body_alter_formpage_top_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalpagehero',
            name='primary_tagline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='generalpagehero',
            name='secondary_tagline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='landingpagehero',
            name='primary_tagline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='landingpagehero',
            name='secondary_tagline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
