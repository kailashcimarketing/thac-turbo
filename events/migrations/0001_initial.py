# Generated by Django 4.2.16 on 2024-10-18 05:26

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=500, null=True, populate_from='title')),
                ('weight', models.IntegerField(default=100)),
            ],
            options={
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=500, null=True, populate_from='title')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('short_description', models.TextField(blank=True, null=True)),
                ('published_date', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_category', to='events.category')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'News',
            },
        ),
    ]
