# Generated by Django 4.2.16 on 2025-05-22 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_vacancies_status_vacancies_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='vacancies',
            options={'verbose_name': 'Vacancies', 'verbose_name_plural': 'Vacancies'},
        ),
    ]
