from django_recaptcha.fields import ReCaptchaField
from django import forms

from contact.models import ContactSubmission
from datetime import datetime


class ContactUsForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = ContactSubmission
        fields = ['full_name', 'phone','email','message','terms_condition']
        
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = '%s' % self.fields[field].label
