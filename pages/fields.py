from .blocks import *


common_blocks = [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('space',SpaceBlock()),
    ('ContentWithVariableWidthBlock',ContentWithVariableWidthBlock()),
    ('TwoColumnBlock',TwoColumnBlock()),
    ('SliderGalleryBlock',SliderGalleryBlock()),
    ('ContentWithImageAlignmentOption',ContentWithImageAlignmentOption()),
]
homepage_stream_fields= common_blocks+ []


generalpage_stream_fields=common_blocks+[]
landingpage_stream_fields=common_blocks+[]

content_holder_stream_fields= [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('CTABannerBlock',CTABannerBlock()),
]