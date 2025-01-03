from wagtail import blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.blocks import PageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

column_width = [
    ('col-lg-1','col-1'),
    ('col-lg-2','col-2'),
    ('col-lg-3','col-3'),
    ('col-lg-4','col-4'),
    ('col-lg-5','col-5'),
    ('col-lg-6','col-6'),
    ('col-lg-7','col-7'),
    ('col-lg-8','col-8'),
    ('col-lg-9','col-9'),
    ('col-lg-10','col-10'),
    ('col-lg-11','col-11'),
    ('col-lg-12','col-12'),
]
column_offset = [
    ('offset-lg-1','offset-1'),
    ('offset-lg-2','offset-2'),
    ('offset-lg-3','offset-3'),
    ('offset-lg-4','offset-4'),
    ('offset-lg-5','offset-5'),
    ('offset-lg-6','offset-6'),

]

top_padding_list =[
    ('pt-0','No padding'),
    ('pt-1','1x'),
    ('pt-2','2x'),
    ('pt-3','3x'),
    ('pt-4','4x'),
    ('pt-5','5x')
]
bottom_padding_list =[
    ('pb-0','No padding'),
    ('pb-1','1x'),
    ('pb-2','2x'),
    ('pb-3','3x'),
    ('pb-4','4x'),
    ('pb-5','5x')
]

class TableItemBlock(blocks.StreamBlock):
    table = TableBlock()


class CustomTableBlock(blocks.StructBlock):
    table_item = TableItemBlock()
    css_class = blocks.CharBlock(required=False, help_text='Table container css class.')

    class Meta:
        label = 'Table'
        template = "pages/blocks/table_block.html"

class HtmlSourceBlock(blocks.StructBlock):
    block_label = blocks.CharBlock(required=False, help_text="This label is for internal reference only and will not be displayed in the output.")
    source = blocks.TextBlock()

    class Meta:
        label = "Html Source"
        icon = "code"
        collapsed = True
        template = "pages/blocks/html_source.html"


class SpaceBlock(blocks.StructBlock):
    height = blocks.IntegerBlock(default=50)
    class Meta:
        label = "Space"
        template = "pages/blocks/space.html"


class DynamicSnippetChooserBlock(blocks.StructBlock):
    css_class = blocks.CharBlock(required=False, help_text='(optional)')
    content = SnippetChooserBlock('pages.DynamicContentSnippet')

    class Meta:
        label = "Dynamic Content Snippet"
        icon = "snippet"
        # closed =True
        template = "pages/blocks/dynamic_snippet_chooser_block.html"                

class ContentBlock(blocks.StructBlock):
    list_style = blocks.ChoiceBlock([
        ('check-list','Checklist'),
    ],default="check-list",required=False)
    content = blocks.RichTextBlock()
    css_class = blocks.CharBlock(required=False)
    class Meta:
        label = "Content"
        template = "pages/blocks/content.html"


class HrefStructValue(blocks.StructValue):
    """Additional logic for our urls."""

    def target(self):
        page_link = self.get('page_link')
        external_link = self.get('external_link')
        document_link = self.get('document_link')
        free_link = self.get('free_link')
        if page_link:
            return ''
        elif external_link:
            return 'target="_blank"'
        elif document_link:
            return 'target="_blank"'
        elif free_link:
            return ''

        return ''

    def detail(self):
        page_link = self.get('page_link')
        external_link = self.get('external_link')
        document_link = self.get('document_link')
        free_link = self.get('free_link')

        if document_link:
            document_size = document_link.file.size / 1024 #bytes to kb
            size_type = 'KB'
            if (document_size  > 1024):
                document_size = document_size / 1024 #kb to mb
                size_type = 'MB'

            if (document_size > 1024): 
                document_size = document_size / 1024 #mb to gb
                size_type = 'gb'
            
            return {'size':float(document_size),'type':str(size_type)}
        elif external_link:
            return ''
        elif page_link:
            return ''
        elif free_link:
            return ''

    def url(self):
        page_link = self.get('page_link')
        external_link = self.get('external_link')
        document_link = self.get('document_link')
        free_link = self.get('free_link')
        if page_link:
            return page_link.url
        elif external_link:
            return external_link
        elif document_link:
            return document_link.url
        elif free_link:
            return free_link
        return 'javascript:void(0);'

    def is_url(self):
        page_link = self.get('page_link')
        external_link = self.get('external_link')
        document_link = self.get('document_link')
        free_link = self.get('free_link')
        if page_link:
            return True
        elif external_link:
            return True
        elif document_link:
            return True
        elif free_link:
            return True
        return False
    


class HrefBlock(blocks.StructBlock):
    page_link = PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)
    document_link = DocumentChooserBlock(required=False)
    free_link = blocks.CharBlock(required=False,help_text='eg. email or phone or #hash')
    
    class Meta:
        icon = "link"
        label = "Urls"
        #form_template = "pages/blocks/admin/href_block.html"
        value_class = HrefStructValue

"""
#Note- do not add theme option to this block.
make new block for theme buttons
"""
class HeadingBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(features=['H1','h2','h3','h4','h5','h6'])
    css_class = blocks.CharBlock(required=False)
    class Meta:
        label= "Heading"
        template = "pages/blocks/heading_block.html"

class SimpleButton(blocks.StructBlock):
    text = blocks.CharBlock(required=False)
    href =  HrefBlock()
    class Meta:
        label = "Simple Button"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock(required=False)
    class Meta:
        label = "Quote"
        template = "pages/blocks/quote_block.html"

class AccordionBlock(blocks.StructBlock):
    items = blocks.ListBlock(blocks.StructBlock([
            ('title',blocks.CharBlock()),
            ('content_blocks',blocks.StreamBlock([
                ('html',HtmlSourceBlock()),
                ('content',ContentBlock()),
                ('heading',HeadingBlock()),
                ('space',SpaceBlock()),
                ('table',CustomTableBlock()),
            ])),
        ])
    )
    class Meta:
        label = "Accordion"
        template = "pages/blocks/accordion_block.html"


class ContentWithVariableWidthBlock(blocks.StructBlock):
    column_width = blocks.ChoiceBlock(column_width,default="col-lg-12")        
    column_offset = blocks.ChoiceBlock(column_offset,required=False)
    
    content_blocks = blocks.StreamBlock([
        ('html',HtmlSourceBlock()),
        ('heading',HeadingBlock()),
        ('space',SpaceBlock()),
        ('content',ContentBlock()),    
        ('accordion',AccordionBlock()),
        ('QuoteBlock',QuoteBlock()),
        ('table',CustomTableBlock()),
    ])
    css_class = blocks.CharBlock(required=False)
    class Meta:
        label = "Content with variable width"
        template = "pages/blocks/content_with_variable_width_block.html"

class ContentStreamBlock(blocks.StreamBlock):
    html = HtmlSourceBlock()
    heading =HeadingBlock()
    content = ContentBlock()
    space = SpaceBlock()
    accordion = AccordionBlock()
    quote = QuoteBlock()
    table = CustomTableBlock()
    

class TwoColumnBlock(blocks.StructBlock):
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    left_column_width = blocks.ChoiceBlock(column_width,required=False,default='col-lg-6')
    left_column_offset = blocks.ChoiceBlock(column_offset,required=False)
    left_column = ContentStreamBlock()
    right_column_width = blocks.ChoiceBlock(column_width,required=False,default='col-lg-6')
    right_column_offset = blocks.ChoiceBlock(column_offset,required=False)
    right_column = ContentStreamBlock()
    css_class = blocks.CharBlock(required=False)  

    class Meta:
        template = 'pages/blocks/two_column_block.html'
        icon = 'grip'
        label = 'Two Columns'


class SliderGalleryBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    items = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock()),
        ('caption',blocks.CharBlock(required=False))
    ]))
    class Meta:
        label = "Slider Gallery"
        template = "pages/blocks/slider_gallery_block.html"



class CTABannerBlock(blocks.StructBlock):
    image = ImageChooserBlock()        
    class Meta:
        label = "CTA Banner"
        template = "pages/blocks/cta_banner_block.html"


class ContentWithImageAlignmentOption(blocks.StructBlock):
    image = ImageChooserBlock()
    alignment = blocks.ChoiceBlock([
        ('left','Left image with right content'),
        ('right','Left content with right image')
    ])
    content = blocks.StreamBlock([
        ('heading',HeadingBlock()),
        ('html',HtmlSourceBlock()),
        ('content',ContentBlock()),
    ])
    class Meta:
        label = "Content with image alignment option"
        template = "pages/blocks/content_with_image_alignment_option_block.html"



class AnnouncementsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    script_title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock()),
        ('href',HrefBlock())
    ]))
    button = SimpleButton()
    class Meta:
        label = "Announcements"
        template = "pages/blocks/announcements_block.html"

class FeaturedSectionBlock(blocks.StructBlock):
    parallax_image = ImageChooserBlock()
    title = blocks.CharBlock()
    highlighted_title = blocks.CharBlock(required=False)
    button = SimpleButton()
    class Meta:
        label = "Featured Section"
        template = "pages/blocks/featured_section_block.html"

class BigScrollBannerBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    script_title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock()),
        ('href',HrefBlock())
    ]))
    button = SimpleButton()
    class Meta:
        label = "Big scroll banner"
        template = "pages/blocks/big_scroll_banner_block.html"

class IconBlock(blocks.StructBlock):
    icon_code = blocks.CharBlock(required=False)
    icon_svg = DocumentChooserBlock(required=False)    
    icon_image = ImageChooserBlock(required=False)
    class Meta:
        label = "Icon"
        template = "pages/blocks/icon_block.html"

class TwoColumnScrollSliderBlock(blocks.StructBlock):
    items = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock()),
        ('icon',ImageChooserBlock()),
        ('pre_title',blocks.CharBlock()),
        ('title',blocks.CharBlock()),
        ('script_title',blocks.CharBlock(required=False)),
        ('text',blocks.RichTextBlock(required=False))
    ]))        
    class Meta:
        label = "Two column scroll slider"
        template = "pages/blocks/two_column_scroll_slider.html"


class FullWidthPromoBannerBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Background Image")
    title = blocks.CharBlock()
    sub_title = blocks.CharBlock()
    text  = blocks.TextBlock()
    button = SimpleButton()
    class Meta:
        template = "pages/blocks/fullwidth_promobanner_block.html"        
        label = "Full width promo banner"
        
class ProfileWithVideoBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    sub_title= blocks.CharBlock()
    image = ImageChooserBlock(label="Profile Picture")
    text = blocks.TextBlock(label="Short Description")
    video_url = blocks.URLBlock()
    video_poster = ImageChooserBlock(required=False)
    button = SimpleButton()

    class Meta:
        label = "Profile with video"
        template = "pages/blocks/profile_with_video_block.html"


class CTACardLinksBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Default backgrund image")
    items = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock(label="Background image")),
        ('icon',ImageChooserBlock()),
        ('title',blocks.CharBlock()),
        ('text',blocks.TextBlock()),
        ('button',SimpleButton()),
    ]))
    class Meta:
        label = "CTA card links"
        template = "pages/blocks/cta_card_links_block.html"


class PromoBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Background image")
    promo_image = ImageChooserBlock()
    title = blocks.CharBlock()
    title2 = blocks.CharBlock()
    text = blocks.TextBlock()
    script_title = blocks.CharBlock(required=False)
    class Meta:
        label = "Promo Banner"
        template = "pages/blocks/promo_banner_block.html"

class LandingPageIntroBlock(blocks.StructBlock):
    background_image = ImageChooserBlock()
    primary_title = blocks.CharBlock()        
    text = blocks.TextBlock(required=False)
    video_url = blocks.URLBlock(help_text="Mp4 Video")
    title = blocks.CharBlock(required=False)
    sub_title = blocks.CharBlock(required=False)
    image = ImageChooserBlock()
    quote = blocks.TextBlock(required=False)
    quote_by = blocks.CharBlock(required=False)
    button = SimpleButton()
    class Meta:
        group = "Landing Page"
        label = "Intro content for landing page"
        template = "pages/blocks/landing_page_intro_block.html"

class InternalpageIntroBlock(blocks.StructBlock):
    title = blocks.CharBlock()        
    sub_title = blocks.CharBlock()
    image = ImageChooserBlock()
    text = blocks.TextBlock()
    class Meta:
        label = "Internal page intro"
        template = "pages/blocks/internal_page_intro_block.html"

        
class ExplorePagesBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    landing_page = PageChooserBlock(required=False)
    class Meta:
        label = "Explore Pages(local navigation)"
        group = "Landing Page"
        template = "pages/blocks/explore_pages_block.html"
    
class QuoteWithImage(blocks.StructBlock):
    quote = blocks.RichTextBlock()
    quote_by = blocks.CharBlock()
    image = ImageChooserBlock()
    class Meta:
        label = "Quote with image"
        template = "pages/blocks/quote_with_image_block.html"


class ContactpageHeroBlock(blocks.StructBlock):
    title = blocks.CharBlock()        
    script_title = blocks.CharBlock()
    image = ImageChooserBlock()
    items = blocks.ListBlock(blocks.StructBlock([
        ('icon',ImageChooserBlock()),
        ('title',blocks.CharBlock()),
        ('text',blocks.TextBlock()),
        ('button',SimpleButton()),
        ('footer_text',blocks.CharBlock(required=False)),
        ('footer_button',SimpleButton())
    ]))
    class Meta:
        label = "Contact page hero section"
        group = "Hero Section"
        template = "pages/blocks/contact_page_hero_block.html"


class StatsCardWithParallaxImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock()
    sub_title = blocks.CharBlock()
    items = blocks.ListBlock(blocks.StructBlock([
        ('pre_title',blocks.CharBlock()),
        ('value',blocks.CharBlock()),
        ('symbol',blocks.CharBlock()),
        ('post_title',blocks.CharBlock()),
        ('text',blocks.TextBlock())
    ]))
    class Meta:
        label = "Stats card with parallax image"
        template = "pages/blocks/stats_card_with_parallax_image_block.html"

class SimpleImageCardwithTextBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    sub_title = blocks.CharBlock()
    items=  blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock()),
        ('text',blocks.TextBlock())
    ]))
    class Meta:
        label = "Simple image and text card grid"
        template = "pages/blocks/simple_image_card_with_text_block.html"


class LeftImageAndRightTextWithBackgroundImageBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    background_image = ImageChooserBlock()
    image = ImageChooserBlock()
    lead_text = blocks.TextBlock()
    text = blocks.TextBlock()
    button = SimpleButton()
    class Meta:
        label = "Left image and right text with background image"        
        template = "pages/blocks/left_image_right_text_with_background_image_block.html"




class StatsCardWithoutParallaxBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    sub_title = blocks.CharBlock()
    text = blocks.TextBlock()
    image = ImageChooserBlock()
    items = blocks.ListBlock(blocks.StructBlock([
        ('pre_title',blocks.CharBlock()),
        ('value',blocks.CharBlock()),
        ('symbol',blocks.CharBlock()),
        ('post_title',blocks.CharBlock()),
        ('text',blocks.TextBlock())
    ]))
    class Meta:
        label = "Stats card without parallax"
        template = "pages/blocks/stats_card_without_parallax_block.html"
    


class FullwidthCTABanner(blocks.StructBlock):
    background_image = ImageChooserBlock()
    title = blocks.CharBlock()
    sub_title = blocks.CharBlock()
    text =blocks.TextBlock()
    button = SimpleButton()
    class Meta:
        label = "Fullwidth CTA banner"
        template = "pages/blocks/fullwidth_cta_banner_block.html"


class GridPhotoGalleryBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    items = blocks.ListBlock(blocks.StructBlock([
            ('image',ImageChooserBlock())
            ]))
    class Meta:
        label = "Grid photo gallery"
        template = "pages/blocks/grid_photo_gallery_block.html"


class VideoBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    script_title = blocks.CharBlock()
    lead_text = blocks.TextBlock()
    poster_image = ImageChooserBlock()
    vide_url = blocks.URLBlock(help_text="MP4 video url")
    class Meta:
        label = "Video"        
        template = "pages/blocks/vide_block.html"

class TwocolumnLeftImageAndRightContent(blocks.StructBlock):
    image = ImageChooserBlock()
    lead_text = blocks.TextBlock()
    text = blocks.TextBlock()
    class Meta:
        group = "Two Columns"
        label = "Left image and right content"        
        template = "pages/blocks/twocolumn_left_image_right_content_block.html"

class TwocolumnListContentBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    items=  blocks.ListBlock(blocks.StructBlock([
        ('title',blocks.CharBlock()),
        ('theme',blocks.ChoiceBlock([
            ('coloured-block--1','Teal'),
            ('coloured-block--2','Peach'),
            ('coloured-block--3','Yellow'),
            ('coloured-block--4','Green'),
            ('coloured-block--5','Orange'),
            ('coloured-block--6','Lilac'),
            ('coloured-block--7','Light Blue'),
            ('coloured-block--8','Turquoise'),
        ])),
        ('list_content',blocks.RichTextBlock())
    ]))
    class Meta:
        label = "List Content"
        template = "pages/blocks/twocolumn_list_content_block.html"

class CTAButton(blocks.StructBlock):
    title = blocks.CharBlock()
    button = SimpleButton()
    class Meta:
        label = "CTA Button"        
        template = "pages/blocks/cta_button_block.html"


class TimelineBlock(blocks.StructBlock):
    items = blocks.ListBlock(blocks.StructBlock([
        ('icon',ImageChooserBlock()),
        ('image',ImageChooserBlock()),
        ('title',blocks.CharBlock()),
        ('button',SimpleButton()),
    ]))
    class Meta:
        label = "Timeline"
        template = "pages/blocks/timeline_block.html"


class FaqBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    items= blocks.ListBlock(blocks.StructBlock([
        ('title',blocks.CharBlock(label="Question")),
        ('content',blocks.RichTextBlock(label="Answer"))
    ]))
    button = SimpleButton()
    class Meta:
        label = "FAQs"
        template = "pages/blocks/faq_block.html"


class ChildVideBlock(blocks.StructBlock):
    poster_image = ImageChooserBlock()
    video_url = blocks.URLBlock()
    class Meta:
        label ="Video"
        template = "pages/blocks/sub_video_block.html"

class ProfileBlock(blocks.StructBlock):
    script_title = blocks.CharBlock()
    image = ImageChooserBlock()
    name = blocks.CharBlock()
    position = blocks.CharBlock()
    class Meta:
        label = "Profile"
        template = "pages/blocks/profile_block.thml"

class ContentWithLeftHeadingBlock(blocks.StructBlock):
    left_title = blocks.CharBlock()
    content = blocks.StreamBlock([
        ('heading',HeadingBlock()),
        ('content',ContentBlock()),
        ('video',ChildVideBlock()),
        ('ProfileBlock',ProfileBlock()),
    ])
    class Meta:
        label = "Content with left heading"
        template = "pages/blocks/content_with_left_heading_block.html"


class HomepageIntroContentBlock(blocks.StructBlock):
    lead_text = blocks.TextBlock()        
    text = blocks.RichTextBlock()
    button= SimpleButton()
    class Meta:
        label = "Homepage intro content"
        template = "pages/blocks/homepage_intro_content_block.html" 