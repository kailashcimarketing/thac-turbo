# Generated by Django 4.2.16 on 2025-02-17 06:51

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_rename_published_date_news_release_date_news_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=wagtail.fields.StreamField([('HtmlSourceBlock', 2), ('QuoteBlock', 4), ('GridPhotoGalleryBlock', 10)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'This label is for internal reference only and will not be displayed in the output.', 'required': False}), 1: ('wagtail.blocks.TextBlock', (), {}), 2: ('wagtail.blocks.StructBlock', [[('block_label', 0), ('source', 1)]], {}), 3: ('wagtail.blocks.CharBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('quote', 1), ('author', 3)]], {}), 5: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('light-theme', 'Light'), ('dark-theme', 'Dark')], 'label': 'background'}), 6: ('wagtail.blocks.CharBlock', (), {}), 7: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 8: ('wagtail.blocks.StructBlock', [[('image', 7)]], {}), 9: ('wagtail.blocks.ListBlock', (8,), {}), 10: ('wagtail.blocks.StructBlock', [[('background', 5), ('title', 6), ('items', 9)]], {})}, null=True),
        ),
    ]
