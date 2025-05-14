from .blocks import *


common_blocks = [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('space',SpaceBlock()),
    ('divider',DividerBlock()),
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
    ('NextPrevBlock',NextPrevBlock()),
    ('ExplorePageswithFlyoutPanelBlock',ExplorePageswithFlyoutPanelBlock()),
    ('LatestNewsBlock',LatestNewsBlock()),
    ('TimetableBlock',TimetableBlock()),
    ('InternalPageNavigationBlock',InternalPageNavigationBlock()),
    ('TutorListBlock',TutorListBlock()),
    ('InstructorListBlock',InstructorListBlock()),
    ('CoacheListBlock',CoacheListBlock()),
    
]
homepage_stream_fields= common_blocks+ [
    ('HomepageIntroContentBlock',HomepageIntroContentBlock()),
    ('HomepageFeaturedEventBlock',HomepageFeaturedEventBlock())
]
contactpage_stream_fields= common_blocks+ [
    ('ContactpageHeroBlock',ContactpageHeroBlock()),
]

events_stream_fields = [
    ('EventQuote',EventQuote()),
    ('EventContentBlocks',EventContentBlocks()),
    ('ProfileBlock',ProfileBlock()),
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('space',SpaceBlock()),
    ('VideoBlock',VideoBlock()),
    ('ContentWithVariableWidthBlock',ContentWithVariableWidthBlock()),
    ('CTAButton',CTAButton()),
]


generalpage_stream_fields=common_blocks+[]
landingpage_stream_fields=common_blocks+[]

newspage_stream_fields=[
   ('HtmlSourceBlock',HtmlSourceBlock()), 
   ('NewsQuoteBlock',NewsQuoteBlock()),
   ('ContentBlock',ContentBlock()),
   ('CTABannerBlock',CTABannerBlock()),
   ('NewsPhotoGalleryBlock',NewsPhotoGalleryBlock()),
   ('NewsProfileBlock',NewsProfileBlock()),
   ('SpaceBlock',SpaceBlock())
]

content_holder_stream_fields= [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('CTABannerBlock',CTABannerBlock()),
    ('CTAButton',CTAButton()),
    ('CTACardLinksBlock',CTACardLinksBlock()),
    ('FullWidthPromoBannerBlock',FullWidthPromoBannerBlock()),
]