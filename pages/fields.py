from .blocks import *


common_blocks = [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('space',SpaceBlock()),
    ('ContentWithVariableWidthBlock',ContentWithVariableWidthBlock()),
    ('TwoColumnBlock',TwoColumnBlock()),
    ('SliderGalleryBlock',SliderGalleryBlock()),
    ('ContentWithImageAlignmentOption',ContentWithImageAlignmentOption()),
    ('AnnouncementsBlock',AnnouncementsBlock()),
    ('FeaturedSectionBlock',FeaturedSectionBlock()),
    ('BigScrollBannerBlock',BigScrollBannerBlock()),
    ('TwoColumnScrollSliderBlock',TwoColumnScrollSliderBlock()),
    ('FullWidthPromoBannerBlock',FullWidthPromoBannerBlock()),
    ('ProfileWithVideoBlock',ProfileWithVideoBlock()),
    ('CTACardLinksBlock',CTACardLinksBlock()),
    ('PromoBlock',PromoBlock()),
    ('LandingPageIntroBlock',LandingPageIntroBlock()),
    ('ExplorePagesBlock',ExplorePagesBlock()),
    ('QuoteWithImage',QuoteWithImage()),
]
homepage_stream_fields= common_blocks+ []


generalpage_stream_fields=common_blocks+[]
landingpage_stream_fields=common_blocks+[]

content_holder_stream_fields= [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('CTABannerBlock',CTABannerBlock()),
]