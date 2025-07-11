# Generated by Django 4.2.16 on 2025-06-05 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('pages', '0164_alter_formpage_bottom_body_alter_formpage_top_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Portal Link',
                'verbose_name_plural': 'Portal Links',
            },
        ),
    ]
