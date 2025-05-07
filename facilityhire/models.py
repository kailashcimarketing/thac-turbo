# models.py
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm, FORM_FIELD_CHOICES
from wagtail.contrib.forms.forms import FormBuilder
from modelcluster.fields import ParentalKey
from django import forms
from wagtail.admin.panels import Panel
from django.template.response import TemplateResponse
from wagtail.contrib.forms.models import AbstractFormSubmission
from django.utils.html import format_html, format_html_join
import json
from wagtail.contrib.forms.views import SubmissionsListView
from django.utils.safestring import mark_safe
from wagtail.fields import StreamField, RichTextField
from pages.fields import generalpage_stream_fields
from home.models import HeroAbstract

class FacilityhireSubmissionsListView(SubmissionsListView):
    template_name = 'facilityhire/admin/default_submissions_list.html'
    results_template_name = "facilityhire/admin/list_submissions.html"
    def get_context_data(self, **kwargs):
        """Return context for view with booking data."""
        context = super().get_context_data(**kwargs)
        submissions = context[self.context_object_name]
        form_fields = self.form_page.get_data_fields()
        booking_fields = self.form_page.get_booking_fields()

        data_rows = []
        context["submissions"] = submissions

        if not self.is_export:
            # HEADINGS
            ordering_by_field = self.get_validated_ordering()
            orderable_fields = self.orderable_fields
            data_headings = []

            for name, label in form_fields:
                order_label = None
                if name in orderable_fields:
                    order = ordering_by_field.get(name)
                    if order:
                        order_label = order[1]
                    else:
                        order_label = "orderable"
                data_headings.append({
                    "name": name,
                    "label": label,
                    "order": order_label,
                })

            # Add booking summary heading
            data_headings.append({"name": "booking_summary", "label": "Booking Summary", "order": None})
            data_headings.append({"name": "booking_details", "label": "Booking Details", "order": None})

            # ROWS
            for submission in submissions:
                form_data = submission.get_data()
                row_fields = []

                # Basic form field values
                for name, label in form_fields:
                    val = form_data.get(name)
                    if isinstance(val, list):
                        val = ", ".join(val)
                    row_fields.append(val)

                # Booking summary (e.g., "2 booking(s) submitted")
                row_fields.append(form_data.get("booking_summary", "—"))

                # Booking detailed view
                bookings = form_data.get("bookings", [])
                booking_lines = []
                for i, booking in enumerate(bookings, start=1):
                    line_parts = [f"<strong>Booking {i}:</strong>"]
                    for tf in booking_fields:
                        label = tf.get("label")
                        val = booking.get(tf.get("name"), "")
                        line_parts.append(f"{label}: {val}")
                    booking_lines.append("<br>".join(line_parts))

                booking_html = "<hr>".join(booking_lines) if booking_lines else "—"
                row_fields.append(mark_safe(booking_html))

                data_rows.append({
                    "model_id": submission.id,
                    "fields": row_fields,
                })

            context.update({
                "form_page": self.form_page,
                "data_headings": data_headings,
                "data_rows": data_rows,
            })

        return context


    
class FacilityhireFormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=list(FORM_FIELD_CHOICES) +
        [
            ('image', 'Upload Image'), ('document', 'File Upload'),
        ]
    )
    page = ParentalKey('FacilityhireFormPage', on_delete=models.CASCADE, related_name='form_fields')      
    

class FacilityhireformpageHero(HeroAbstract):
    page = ParentalKey('FacilityhireFormPage', related_name='facilityhireformpage_hero')

class FacilityhireFormPage(AbstractEmailForm):
    submissions_list_view_class = FacilityhireSubmissionsListView
    thank_you_text = RichTextField(blank=True)
    booking_field_help_text = RichTextField(blank=True, help_text="Help text to display above booking fields")
    top_body = StreamField(generalpage_stream_fields,null=True,blank=True)
    bottom_body = StreamField(generalpage_stream_fields,null=True,blank=True)
    
    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('facilityhireformpage_hero', label='Hero Images', panels=[
            FieldPanel('image'),
            FieldPanel('background_video_url'),   
            FieldPanel('title'),
            FieldPanel('script_title'),
            FieldPanel('primary_tagline'),
            FieldPanel('secondary_tagline'),   
        ],max_num=1),
        
        FieldPanel('booking_field_help_text'),
        MultiFieldPanel([
            InlinePanel('form_fields'),
        ], heading="Form Fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], heading="Email Settings"),
        FieldPanel('top_body'),
        FieldPanel('bottom_body'),
    ]

    def get_hero(self):
        if self.facilityhireformpage_hero.all():
            return self.facilityhireformpage_hero.all()
        else:
            return False
    
    def get_hero_image(self):
        if self.get_hero():
            return self.get_hero()[0]
        
        return False
    
    def get_form_class(self):
        form_class = super().get_form_class()
        
        # Add a field to store the number of bookings
        form_class.base_fields['booking_count'] = forms.IntegerField(
            widget=forms.HiddenInput(),
            initial=1
        )
        
        return form_class
    
    def get_form_fields(self):
        return self.form_fields.all()
    
    def get_booking_fields(self):
        # Define the fields that will be repeated for each booking
        return [
            {
                'name': 'start_date',
                'label': 'Start Date',
                'field_type': 'date',
                'required': True,
            },
            {
                'name': 'end_date',
                'label': 'End Date',
                'field_type': 'date',
                'required': True,
            },
            {
                'name': 'frequency_of_booking',
                'label': 'Frequency of Booking (i.e. weekly)',
                'field_type': 'singleline',
                'required': True,
            },
            {
                'name': 'start_time',
                'label': 'Start Time',
                'field_type': 'text',
                'required': True,
            },
            {
                'name': 'finish_time',
                'label': 'Finish Time',
                'field_type': 'text',
                'required': True,
            },
            {
                'name': 'number_of_participants',
                'label': 'Number of Participants',
                'field_type': 'number',
                'required': True,
            },
            
            
        ]
    
    def process_form_submission(self, form):
        """
        Process and store form submission data with booking information
        """
        # First, get the booking data
        booking_count = int(form.cleaned_data['booking_count'])
        booking_data = []
        
        for i in range(1, booking_count + 1):
            booking = {
                'start_date': form.cleaned_data.get(f'booking_{i}_start_date', ''),
                'end_date': form.cleaned_data.get(f'booking_{i}_end_date', ''),
                'frequency_of_booking': form.cleaned_data.get(f'booking_{i}_frequency_of_booking', ''),
                'start_time': form.cleaned_data.get(f'booking_{i}_start_time', ''),
                'finish_time': form.cleaned_data.get(f'booking_{i}_finish_time', ''),
                'number_of_participants': form.cleaned_data.get(f'booking_{i}_number_of_participants', ''),
            }
            booking_data.append(booking)
            
            # Remove booking fields from form.cleaned_data to prevent duplicates in form_data
            for field_name in ['start_date', 'end_date', 'frequency_of_booking', 'start_time','finish_time','number_of_participants']:
                form.cleaned_data.pop(f'booking_{i}_{field_name}', None)
        
        # Add consolidated booking data to form.cleaned_data
        form.cleaned_data['bookings'] = booking_data
        form.cleaned_data['booking_summary'] = f"{booking_count} booking(s) submitted"
        
        # Use the parent class's method to create the submission
        return super().process_form_submission(form)
    
    def serve(self, request):
        if request.method == 'POST':
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)

            try:
                booking_count = int(request.POST.get('booking_count', 1))
            except ValueError:
                booking_count = 1

            for i in range(1, booking_count + 1):
                form.fields[f'booking_{i}_start_date'] = forms.DateField(
                    label=f"Booking {i} Start Date", required=True
                )
                form.fields[f'booking_{i}_end_date'] = forms.DateField(
                    label=f"Booking {i} End Date", required=True
                )
                
                form.fields[f'booking_{i}_frequency_of_booking'] = forms.CharField(
                    label=f"Booking {i} Frequency of Booking", required=True
                )
                form.fields[f'booking_{i}_start_time'] = forms.EmailField(
                    label=f"Booking {i} Start Time", required=True
                )
                form.fields[f'booking_{i}_finish_time'] = forms.EmailField(
                    label=f"Booking {i} Finish Time", required=True
                )
                form.fields[f'booking_{i}_number_of_participants'] = forms.EmailField(
                    label=f"Booking {i} Number of Participants", required=True
                )
            
            if form.is_valid():
                # Process the form data
                form_submission = self.process_form_submission(form)
                
                # Get the booking data and process it
                booking_count = int(form.cleaned_data['booking_count'])
                booking_data = []
                
                for i in range(1, booking_count + 1):
                    booking = {
                        'start_date': form.cleaned_data.get(f'booking_{i}_start_date', ''),
                        'end_date': form.cleaned_data.get(f'booking_{i}_end_date', ''),
                        'frequency_of_booking': form.cleaned_data.get(f'booking_{i}_frequency_of_booking', ''),
                        'start_time': form.cleaned_data.get(f'booking_{i}_start_time', ''),
                        'finish_time': form.cleaned_data.get(f'booking_{i}_finish_time', ''),
                        'number_of_participants': form.cleaned_data.get(f'booking_{i}_number_of_participants', ''),
                    }
                    booking_data.append(booking)
                
                # Add booking data to the form submission object if needed
                form_submission.bookings = booking_data  # You can save this data to a custom field in the submission model, if desired.

                # You can process it further here if needed (save to a database or send in emails, etc.)
                
                return self.render_landing_page(request, form_submission)
        
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form
        context['booking_fields'] = self.get_booking_fields()  # Display booking fields on the form
        return TemplateResponse(request, self.get_template(request), context)

    
    class Meta:
        verbose_name = "Facility Hire Form Page"