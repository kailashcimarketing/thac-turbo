from django.db import models
from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from pages.fields import homepage_stream_fields
from home.models import HeroAbstract
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from django.utils.html import strip_tags

# Create your models here.
class ContactSubmission(models.Model):
    full_name = models.CharField(null=True,blank=False,max_length=255)
    email = models.EmailField(null=True,blank=False)
    phone =  models.CharField(null=True,blank=False,max_length=25)
    message = models.TextField(null=True,blank=True)
    terms_condition = models.BooleanField(default=True,blank=False)
    created = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
        ordering = ['-created',]

    def send_email(self,page):
        context = {"contact": self}
        html_template = get_template('contact/email/contact.html')
        text_template = get_template('contact/email/contact.txt')
        email_html = html_template.render(context)
        email_text = text_template.render(context)
        #send_to_email_addresses = [settings.CONTACT_EMAIL]
        if page.notification_to_address:
            to_addresses = [x.strip() for x in page.notification_to_address.split(',')]
        else:
            to_addresses = [page.notification_to_address]
        from_email_address = page.notification_from_address
        email = EmailMultiAlternatives(subject=page.notification_subject, 
                                    body=email_text,
                                    from_email=from_email_address, 
                                    to=to_addresses,
                                    reply_to=[from_email_address],
                                    )
        email.attach_alternative(email_html, "text/html")
        email.send()

        #autoresponse to user
        user_email_html = page.autoresponder_content
        user_email_text = strip_tags(user_email_html)
        automail_subject = page.autoresponder_subject
        automail_from  = page.autoresponder_from_email
        automail_to = [self.email]
        useremail = EmailMultiAlternatives(automail_subject, 
                                        body=user_email_text,
                                    from_email = automail_from, 
                                    to =automail_to,
                                    reply_to=[automail_from],
                                    )
        useremail.attach_alternative(user_email_html, "text/html")
        useremail.send()   


class ContactPage(Page):
    # intro = RichTextField(blank=True)
    thankyou_message = RichTextField()
    #auto
    autoresponder_from_email = models.CharField(max_length=100, null=True, blank=True)
    autoresponder_subject = models.CharField(max_length=200, null=True, blank=True)
    autoresponder_content = RichTextField(blank=True)
    #notification
    notification_from_address = models.CharField(max_length=100, null=True, blank=True)
    notification_to_address = models.CharField(max_length=200, null=True, blank=True)
    notification_subject = models.CharField(max_length=500,null=True,blank=True)
    body = StreamField(homepage_stream_fields,null=True,blank=True)
    bottom_body = StreamField(homepage_stream_fields,null=True,blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('thankyou_message'),
        MultiFieldPanel([
        FieldPanel('autoresponder_from_email'),
        FieldPanel('autoresponder_subject'),
        FieldPanel('autoresponder_content'),
        ],'Autoresponder mail notification'),
        MultiFieldPanel([
        FieldPanel('notification_from_address'),
        FieldPanel('notification_to_address'),
        FieldPanel('notification_subject'),
        ],'Mail notification'),
        FieldPanel('body'),
        FieldPanel('bottom_body'),
    ]

    class Meta:
        verbose_name = "Contact Page"

    def get_hero_image(self):
        if self.contactpage_hero.all():
            return self.contactpage_hero.all()[0]
        else:
            return False 
        
    def get_hero(self):
        return False

    def serve(self, request):
        from contact.forms import ContactUsForm

        if request.method == 'POST':
            form = ContactUsForm(request.POST)
            if form.is_valid():
                contact = form.save()
                contact.send_email(self)
                return render(request, 'contact/thankyou.html', {
                    'page': self,
                    'contact': contact,
                })
        else:
            form = ContactUsForm()

        return render(request, 'contact/contact_form.html', {
            'page': self,
            'form': form,
        })
