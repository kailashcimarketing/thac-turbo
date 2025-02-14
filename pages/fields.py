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
    ('ExplorePagesInternalBlock',ExplorePagesInternalBlock()),
    ('QuoteWithImage',QuoteWithImage()),
    ('InternalpageIntroBlock',InternalpageIntroBlock()),
    ('StatsCardWithParallaxImageBlock',StatsCardWithParallaxImageBlock()),
    ('SimpleImageCardwithTextBlock',SimpleImageCardwithTextBlock()),
    ('LeftImageAndRightTextWithBackgroundImageBlock',LeftImageAndRightTextWithBackgroundImageBlock()),
    ('StatsCardWithoutParallaxBlock',StatsCardWithoutParallaxBlock()),
    ('GridPhotoGalleryBlock',GridPhotoGalleryBlock()),
    ('LeadParagraphCapsBlock',LeadParagraphCapsBlock()),
    ('CentredTitleBlock',CentredTitleBlock()),
    ('VideoBlock',VideoBlock()),
    ('TwocolumnLeftImageAndRightContent',TwocolumnLeftImageAndRightContent()),
    ('TwocolumnListContentBlock',TwocolumnListContentBlock()),
    ('CTAButton',CTAButton()),
    ('TimelineBlock',TimelineBlock()),
    ('FaqBlock',FaqBlock()),
    ('ContentWithLeftHeadingBlock',ContentWithLeftHeadingBlock()),
    ('VacanciesListBlock',VacanciesListBlock()),
    ('TeamListBlock',TeamListBlock()),
    ('CustomTableBlock',CustomTableBlock()),
    ('PDFFlipBookBlock',PDFFlipBookBlock()),
    ('DynamicSnippetChooserBlock',DynamicSnippetChooserBlock()),
    ('NextPrevBlock',NextPrevBlock())
]
homepage_stream_fields= common_blocks+ [
    ('HomepageIntroContentBlock',HomepageIntroContentBlock()),
]
contactpage_stream_fields= common_blocks+ [
    ('ContactpageHeroBlock',ContactpageHeroBlock()),
]

events_stream_fields = [
    ('EventQuote',EventQuote()),
    ('EventContentBlocks',EventContentBlocks()),
    ('ProfileBlock',ProfileBlock()),
]


generalpage_stream_fields=common_blocks+[]
landingpage_stream_fields=common_blocks+[]

content_holder_stream_fields= [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('CTABannerBlock',CTABannerBlock()),
    ('CTAButton',CTAButton()),
    ('CTACardLinksBlock',CTACardLinksBlock()),
    ('FullWidthPromoBannerBlock',FullWidthPromoBannerBlock()),
]