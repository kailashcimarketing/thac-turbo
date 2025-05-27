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
background_color =[
        ('light-theme','Light'),
        ('dark-theme','Dark'),
        ('light-teal-theme','Light Teal')
    ]

theme_layout =[
        ('light-theme','White'),
        ('dark-theme','Navy'),
        ('light-teal-theme','Light Teal')
    ]
divider_background =[
        ('light-theme','White'),
        ('dark-theme','Navy'),
        ('light-teal-theme','Light Teal'),
        ('light-grey','Light Grey'),
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
        
class IframeBlock(blocks.StructBlock):
    source = blocks.TextBlock()
    class Meta:
        label = "Iframe"
        icon = "code"
        collapsed = True
        template = "pages/blocks/iframe_source.html"


class SpaceBlock(blocks.StructBlock):
    height = blocks.IntegerBlock(default=50)
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    class Meta:
        label = "Space"
        template = "pages/blocks/space.html"
        
class DividerBlock(blocks.StructBlock):
    #height = blocks.IntegerBlock(default=50)
    background = blocks.ChoiceBlock(divider_background,label="Background",default="light-theme")
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    with_container = blocks.BooleanBlock(default=False,required=False)
    class Meta:
        label = "Divider"
        template = "pages/blocks/divider_block.html"

class LeadTextBlock(blocks.StructBlock):
    text = blocks.TextBlock()
    class Meta:
        label = "Lead Text"
        template = "pages/blocks/lead_text_block.html"


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
    heading = blocks.RichTextBlock(features=['h1','h2','h3','h4','h5','h6'])
    css_class = blocks.CharBlock(required=False)
    class Meta:
        label= "Heading"
        template = "pages/blocks/heading_block.html"

class SimpleButton(blocks.StructBlock):
    text = blocks.CharBlock(required=False)
    href =  HrefBlock()
    class Meta:
        label = "Simple Button"
        template = "pages/blocks/simple_button_block.html"

class ThemeButton(blocks.StructBlock):
    text = blocks.CharBlock(required=False)        
    theme = blocks.ChoiceBlock([
        ('btn btn--dark-blue','Solid blue'),
        ('btn btn--fifth','Solid white'),
        ('btn btn--secondary','Solid teal'),
        ('btn btn--third','Teal outline'),
        ('btn btn-download','Download'),
        ('btn btn-external-link','External link'),
        ('link','Link'),
    ],required=False)
    href = HrefBlock()
    class Meta:
        label = "Theme Button"
        template = "pages/blocks/theme_button.html"
        
class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock(required=False)
    class Meta:
        label = "Quote"
        template = "pages/blocks/quote_block.html"

class NewsQuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock(required=False)
    class Meta:
        label = "Quote"
        template = "pages/blocks/news_quote_block.html"
        
class DownloadList(blocks.StructBlock):
    items = blocks.ListBlock(blocks.StructBlock([
        ('label',blocks.CharBlock()),
        ('document',DocumentChooserBlock(required=False)),
        ('external_link',blocks.URLBlock(required=False))
    ]))
    class Meta:
        label = "Download List"
        icon = "download"
        template = "pages/blocks/download_list.html"

class ChildImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    class Meta:
        label = "Image"
        template = "pages/blocks/child_image_block.html"
        
class ExternalLinkListingBlock(blocks.StructBlock):
    items = blocks.ListBlock(blocks.StructBlock([
        ('title',blocks.CharBlock(required=False)),
        ('links',blocks.ListBlock(blocks.StructBlock([
            ('label', blocks.CharBlock()),
            ('external_link',blocks.URLBlock())
        ])))
    ]))
    class Meta:
        label = "External Link List"
        template = "pages/blocks/external_link_list_block.html"        
               
class AccordionBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    items = blocks.ListBlock(blocks.StructBlock([
            ('title',blocks.CharBlock()),
            ('content_blocks',blocks.StreamBlock([
                ('html',HtmlSourceBlock()),
                ('iframe',IframeBlock()),
                ('content',ContentBlock()),
                ('heading',HeadingBlock()),
                ('space',SpaceBlock()),
                ('divider',DividerBlock()),
                ('table',CustomTableBlock()),
                ('image',ChildImageBlock()),
                ('DownloadList',DownloadList()),
                ('ThemeButton',ThemeButton()),
                ('ExternalLinkListingBlock',ExternalLinkListingBlock()),
            ])),
        ])
    )
    class Meta:
        label = "Accordion"
        template = "pages/blocks/accordion_block.html"

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

class LeadParagraphCapsBlock(blocks.StructBlock):
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    lead_text = blocks.TextBlock()
    class Meta:
        label = "lead paragraph in all caps"        
        template = "pages/blocks/lead_paragraph_caps_block.html"

class ContentWithVariableWidthBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    column_width = blocks.ChoiceBlock(column_width,default="col-lg-12")        
    column_offset = blocks.ChoiceBlock(column_offset,required=False)
    
    
    content_blocks = blocks.StreamBlock([
        ('html',HtmlSourceBlock()),
        ('iframe',IframeBlock()),
        ('heading',HeadingBlock()),
        ('space',SpaceBlock()),
        ('divider',DividerBlock()),
        ('content',ContentBlock()),    
        ('accordion',AccordionBlock()),
        ('QuoteBlock',QuoteBlock()),
        ('table',CustomTableBlock()),
        ('DownloadList',DownloadList()),
        ('ChildImageBlock',ChildImageBlock()),
        ('ThemeButton',ThemeButton()),
        ('LeadParagraphCapsBlock',LeadParagraphCapsBlock()),
        ('LeadTextBlock',LeadTextBlock()),
    ])
    css_class = blocks.CharBlock(required=False)
    class Meta:
        label = "Content with variable width"
        template = "pages/blocks/content_with_variable_width_block.html"


        
class ContentStreamBlock(blocks.StreamBlock):
    html = HtmlSourceBlock()
    iframe = IframeBlock()    
    heading =HeadingBlock()
    content = ContentBlock()
    space = SpaceBlock()
    divider = DividerBlock()
    accordion = AccordionBlock()
    quote = QuoteBlock()
    table = CustomTableBlock()
    image = ChildImageBlock()
    downloadlist = DownloadList()
    themebutton = ThemeButton()
    LeadParagraphCapsBlock = LeadParagraphCapsBlock()
    LeadTextBlock = LeadTextBlock()
    ExternalLinkListingBlock = ExternalLinkListingBlock()
    

class TwoColumnBlock(blocks.StructBlock):    
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
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
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
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
        ('iframe',IframeBlock()),
        ('divider',DividerBlock()),
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
        ('event',SnippetChooserBlock('events.Events',required=False)),
        ('href',HrefBlock())
    ]))
    button = SimpleButton()
    class Meta:
        label = "Announcements"
        template = "pages/blocks/announcements_block.html"
        
class HomepageFeaturedEventBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    script_title = blocks.CharBlock(required=False)
    items = blocks.StaticBlock()
    button = SimpleButton()
    class Meta:
        label = "Home page Featured Event"
        template = "pages/blocks/homepage_featured_event_block.html"

class FeaturedSectionBlock(blocks.StructBlock):
    light_theme = blocks.BooleanBlock(required=False)
    parallax_image = ImageChooserBlock()
    background_opacity = blocks.CharBlock(required=False)
    title = blocks.CharBlock()
    highlighted_title = blocks.CharBlock(required=False)
    button = SimpleButton()    
    class Meta:
        label = "Featured Section"
        template = "pages/blocks/featured_section_block.html"

class BigScrollBannerBlock(blocks.StructBlock):
    theme = blocks.ChoiceBlock([
        ('primary','Primary'),
        ('secondary','Secondary'),
    ],default='primary')
    title = blocks.CharBlock(required=False)
    script_title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.StructBlock([
        ('title',blocks.CharBlock(required=False)),
        ('image',ImageChooserBlock()),
        ('href',HrefBlock())
    ]))
    button = SimpleButton()
    class Meta:
        label = "Big vertical scroll banner"
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

"""class FullwidthCTABanner(blocks.StructBlock):
    background_image = ImageChooserBlock()
    title = blocks.CharBlock()
    sub_title = blocks.CharBlock()
    text =blocks.TextBlock()
    button = SimpleButton()
    class Meta:
        label = "Fullwidth CTA banner"
        template = "pages/blocks/fullwidth_cta_banner_block.html"        
"""
        
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
        
        
class NewsProfileBlock(blocks.StructBlock):
    sign= blocks.CharBlock(required=False)
    image = ImageChooserBlock(label="Profile Picture")
    position = blocks.CharBlock(required=False)

    class Meta:
        label = "News Profile"
        template = "pages/blocks/news_profile_block.html"


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
    image = ImageChooserBlock(label="Background image")
    title = blocks.CharBlock(required=False)
    landing_page = PageChooserBlock(required=False)
    class Meta:
        label = "Explore Pages(local navigation)"
        group = "Landing Page"
        template = "pages/blocks/explore_pages_block.html"
        
class ExplorePageswithFlyoutPanelBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Background image")
    title = blocks.CharBlock(required=False)
    script_title =blocks.CharBlock(required=False)    
    items = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock(label="Image")),
        ('title',blocks.CharBlock()),
        ('text',blocks.TextBlock(required=False)),
        ('detail_page',PageChooserBlock(required=False,label="Page")),
        ('button',SimpleButton()),
    ]))
    class Meta:
        label = "Explore Pages with Flyout Panel"
        group = "Landing Page"
        template = "pages/blocks/explore_pages_with_flyout_panel_block.html"

class ExplorePagesInternalBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Background image")
    title = blocks.CharBlock(required=False)
    landing_page = PageChooserBlock(required=False)
    class Meta:
        label = "Internal Explore Pages(local navigation)"
        template = "pages/blocks/explore_pages_internal_block.html"        
    
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
    facebook_url = blocks.CharBlock(required=False)
    instagram_url = blocks.CharBlock(required=False)
    vimeo_url = blocks.CharBlock(required=False)
    linkedin_url = blocks.CharBlock(required=False)
    youtube_url = blocks.CharBlock(required=False)
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

class GridPhotoGalleryBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Column'),
        ('col-lg-3','Four Column')
    ],label="layout",default="col-lg-3")
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.StructBlock([
            ('image',ImageChooserBlock())
            ]))
    class Meta:
        label = "Photo gallery grid"
        template = "pages/blocks/grid_photo_gallery_block.html"
        
        
class NewsPhotoGalleryBlock(blocks.StructBlock):
    #items = blocks.ListBlock(blocks.StructBlock([('image',ImageChooserBlock())            ]),required=False)
    show_photo_gallery = blocks.StaticBlock()
    class Meta:
        label = "Photo gallery grid"
        help_text= "Add this block between content to place photo gallery images uploaded in gallery images section"
        template = "pages/blocks/news_photo_gallery_block.html"

class CentredTitleBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    title = blocks.CharBlock()
    script_title = blocks.CharBlock()    
    class Meta:
        label = "Centred Title Block"        
        template = "pages/blocks/centred_title_block.html"
        

        
class VideoBlock(blocks.StructBlock):
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    layout = blocks.ChoiceBlock([
        ('container','Container'),
        ('container-fluid','Fullwidth')
    ],label="layout",default="container")
    poster_image = ImageChooserBlock(required=False)
    video_url = blocks.URLBlock(help_text="MP4 video url")
    class Meta:
        label = "Video"        
        template = "pages/blocks/video_block.html"

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
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    title = blocks.CharBlock()
    sub_title =blocks.CharBlock(required=False)
    button = SimpleButton()
    class Meta:
        label = "CTA Button"        
        template = "pages/blocks/cta_button_block.html"


class TimelineBlock(blocks.StructBlock):
    text = blocks.TextBlock()
    items = blocks.ListBlock(blocks.StructBlock([
        ('icon',ImageChooserBlock()),
        ('image',ImageChooserBlock()),
        ('video_url',blocks.URLBlock(required=False,help_text='Mp4 video')),
        ('title',blocks.CharBlock()),
        ('button',SimpleButton()),
    ]))
    class Meta:
        label = "Timeline"
        template = "pages/blocks/timeline_block.html"





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
        template = "pages/blocks/profile_block.html"

class ContentWithLeftHeadingBlock(blocks.StructBlock):
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    left_title = blocks.CharBlock()
    left_title_css_class = blocks.CharBlock(required=False)
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    
    content = blocks.StreamBlock([
        ('html',HtmlSourceBlock()),
        ('iframe',IframeBlock()),
        ('heading',HeadingBlock()),
        ('content',ContentBlock()),
        ('video',ChildVideBlock()),
        ('QuoteBlock',QuoteBlock()),
        ('ProfileBlock',ProfileBlock()),
        ('ChildImageBlock',ChildImageBlock()),
        ('space',SpaceBlock()),
        ('divider',DividerBlock()),
        ('DownloadList',DownloadList()),
        ('button',ThemeButton()),
        ('external_links',ExternalLinkListingBlock()),
        ('accordion',AccordionBlock()),
        
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


class VacanciesListBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    items = blocks.StaticBlock()
    class Meta:
        label = "List all vacancies"
        template = "pages/blocks/all_vacancies_block.html"


class TeamListBlock(blocks.StructBlock): 
    title = blocks.CharBlock(required=False)   
    category = SnippetChooserBlock('team.Category',required=False)
    exclude = SnippetChooserBlock('team.Category',required=False)
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Columns'),
        ('col-lg-3','Four columns'),
    ],default='col-lg-3')
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    items = blocks.StaticBlock()
    class Meta:
        label = "List all team"
        group = 'Team'
        template = "pages/blocks/all_team_list.html"

class CoacheListBlock(blocks.StructBlock): 
    title = blocks.CharBlock(required=False)   
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Columns'),
        ('col-lg-3','Four columns'),
    ],default='col-lg-3')
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    class Meta:
        label = "Coaches List"
        group = 'Team'
        template = "pages/blocks/coache_list_block.html"

class TutorListBlock(blocks.StructBlock): 
    title = blocks.CharBlock(required=False)  
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Columns'),
        ('col-lg-3','Four columns'),
    ],default='col-lg-3') 
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    class Meta:
        label = "Tutor List"
        group = 'Team'
        template = "pages/blocks/tutor_list_block.html"

class BoardmemberListBlock(blocks.StructBlock): 
    title = blocks.CharBlock(required=False)  
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Columns'),
        ('col-lg-3','Four columns'),
    ],default='col-lg-3') 
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    class Meta:
        label = "Boardmember List"
        group = 'Team'
        template = "pages/blocks/boardmember_list_block.html"        




class InstructorListBlock(blocks.StructBlock): 
    title = blocks.CharBlock(required=False)   
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Columns'),
        ('col-lg-3','Four columns'),
    ],default='col-lg-3')
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    class Meta:
        label = "Instructor List"
        group = 'Team'
        template = "pages/blocks/instructor_list_block.html"
        
class LatestNewsBlock(blocks.StructBlock): 
    title = blocks.CharBlock(required=False)   
    category = SnippetChooserBlock('news.Category',required=False)
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    limit = blocks.IntegerBlock(default=3)
    items = blocks.StaticBlock()
    
    class Meta:
        label = "Latest News"
        template = "pages/blocks/latest_news_block.html"


class PDFFlipBookBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    title = blocks.CharBlock()
    html = HtmlSourceBlock()
    class Meta:
        label ="PDF flip book"
        template = "pages/blocks/pdf_flip_book_block.html"




class EventQuote(blocks.StructBlock):
    quote = blocks.CharBlock()
    author = blocks.CharBlock(required=False)
    class Meta:
        label = "Quote"
        template = "pages/blocks/events/quote_block.html"

class EventContentBlocks(blocks.StreamBlock):
    content = blocks.RichTextBlock()        
    gallery = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock())
    ]))
    
    class Meta:
        label  = "Content"
        template = "pages/blocks/events/content_block.html"
        
class NextPrevBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    background_image = ImageChooserBlock(required=False)
      
    class Meta:
        label = "Next Prev"    
        template = "pages/blocks/next_prev.html"

class DayContentBlock(blocks.StructBlock):
    text = blocks.TextBlock(required=False)
    category = blocks.ChoiceBlock([
        ('athletics','Athletics'),
        ('basketball','Basketball'),
        ('football','Bootball'),
        ('netball','Netball'),
        ('tennis','Tennis'),
        ('volleyball','Volleyball'),
    ],required=False)

class TimetableBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    rows = blocks.ListBlock(blocks.StructBlock([
        ('time',blocks.CharBlock(required=False)),
        ('monday',DayContentBlock()),
        ('tuesday',DayContentBlock()),
        ('wednesday',DayContentBlock()),
        ('thursday',DayContentBlock()),
        ('friday',DayContentBlock()),
    ]))

    class Meta:
        label = "Timetable"
        template = "pages/blocks/timetable_block.html"
        

class InternalPageNavigationBlock(blocks.StructBlock):
    link_label = blocks.CharBlock(help_text='Text to display for this menu link (e.g., "About", "Contact")')
    class Meta:
        label = "Internal nagivation link"
        template = "pages/blocks/internal_navigation_link_block.html"
        
class ExternalLinkThumbnailsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="dark-theme")
    top_padding = blocks.ChoiceBlock(top_padding_list,required=False)
    bottom_padding = blocks.ChoiceBlock(bottom_padding_list,required=False)
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Columns'),
        ('col-lg-3','Four columns'),
    ],default='col-lg-3') 
    items = blocks.ListBlock(blocks.StructBlock([
        ('image',ImageChooserBlock(label="Image")),
        ('title',blocks.CharBlock()),
        ('external_link',blocks.URLBlock(required=False)),
    ]))
    class Meta:
        label = "External Link Thumbnails"
        template = "pages/blocks/external_link_thumbnails_block.html"


class GalleryBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(theme_layout,label="Background",default="light-theme")
    layout = blocks.ChoiceBlock([
        ('col-lg-4','Three Column'),
        ('col-lg-3','Four Column')
    ],label="layout",default="col-lg-3")
    title = blocks.CharBlock(required=False)
    photo_gallery = SnippetChooserBlock('pages.PhotoGallery')
    class Meta:
        label = "Photo Gallery Grid (snippet)"
        template = "pages/blocks/photo_gallery_grid.html"        