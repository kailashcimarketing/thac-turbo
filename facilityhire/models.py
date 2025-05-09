# models.py
from django.db import models
from wagtail.models import Page, Collection
from os.path import splitext
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
from wagtail.images.fields import WagtailImageField
from django.forms import FileField, CharField, ChoiceField
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from django.utils.html import format_html
from django.urls import reverse

class FacilityhireSubmissionsListView(SubmissionsListView):
    template_name = 'facilityhire/admin/default_submissions_list.html'
    results_template_name = "facilityhire/admin/list_submissions.html"

    def get_context_data(self, **kwargs):
        """Return context for view with booking data."""
        context = super().get_context_data(**kwargs)

        

        ### booking fields listing script
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
            ### booking fields listing script end

            ### file / document script 
            # generate a list of field types, the first being the injected 'submission date'
            field_types = ['submission_date'] + [field.field_type for field in self.form_page.get_form_fields()]
            data_rows = context['data_rows']

            ImageModel = get_image_model()
            DocumentModel = get_document_model()

            for data_row in data_rows:

                fields = data_row['fields']

                for idx, (value, field_type) in enumerate(zip(fields, field_types)):
                    if field_type == 'image' and value:
                        image = ImageModel.objects.get(pk=value)
                        rendition = image.get_rendition(
                            'fill-100x75|jpegquality-40')
                        preview_url = rendition.url
                        url = reverse('wagtailimages:edit', args=(image.id,))
                        # build up a link to the image, using the image title & id
                        fields[idx] = format_html(
                            "<a href='{}'><img alt='Uploaded image - {}' src='{}' /></a>",
                            url,
                            image.title,
                            preview_url,
                        )
                    elif field_type == 'document' and value:
                        document = DocumentModel.objects.get(pk=value)
                        url = reverse('wagtaildocs:edit', args=(document.id,))
                        fields[idx] = format_html(
                            "<a href='{}'>{}</a>",
                            url,
                            document.title,
                        )
            ### file / document script end 
        
        return context


    
class FacilityhireFormField(AbstractFormField):
    help_text = models.TextField(
        verbose_name="help text", blank=True
    )
    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=list(FORM_FIELD_CHOICES) +
        [
            ('image', 'Upload Image'), ('document', 'File Upload'), ('heading', 'Heading')
        ]
    )
    page = ParentalKey('FacilityhireFormPage', on_delete=models.CASCADE, related_name='form_fields')    

class CustomFormBuilder(FormBuilder):
    def create_image_field(self, field, options):
        return WagtailImageField(**options)

    def create_document_field(self, field, options):
        return FileField(**options) 
    
    def create_heading_field(self, field, options):
        return CharField(widget=forms.HiddenInput(attrs={'data_type': 'heading'}), **options) 
    

class FacilityhireformpageHero(HeroAbstract):
    page = ParentalKey('FacilityhireFormPage', related_name='facilityhireformpage_hero')

class FacilityhireFormPage(AbstractEmailForm):
    submissions_list_view_class = FacilityhireSubmissionsListView
    form_builder = CustomFormBuilder
    thank_you_text = RichTextField(blank=True)
    thankyou_message = RichTextField(blank=True)
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
        FieldPanel('thankyou_message'),
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
    
    def get_child_pages(self):
        return self.get_children().live().filter(show_in_menus=True)
    
    def get_form_fields(self):
        return self.form_fields.all()
    
    def get_uploaded_image_collection(self):
        """
        Returns a Wagtail Collection, using this form's saved value if present,
        otherwise returns the 'Root' Collection.
        """
       # collection = self.uploaded_image_collection
        collection = Collection.objects.get(name__exact='uploads')
        return collection or Collection.get_first_root_node()
    
    @staticmethod
    def get_image_title(filename):
        """
        Generates a usable title from the filename of an image upload.
        Note: The filename will be provided as a 'path/to/file.jpg'
        """

        if filename:
            result = splitext(filename)[0]
            result = result.replace('-', ' ').replace('_', ' ')
            return result.title()
        return ''
    
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



        ####### submission script 
        cleaned_data = form.cleaned_data
        document_list = []
        images_list = []
        for name, field in form.fields.items():
            if isinstance(field, WagtailImageField):
                image_file_data = cleaned_data[name]
                if image_file_data:
                    ImageModel = get_image_model()

                    kwargs = {
                        'file': cleaned_data[name],
                        'title': self.get_image_title(cleaned_data[name].name),
                        'collection': self.get_uploaded_image_collection(),
                    }

                    if form.user and not form.user.is_anonymous:
                        kwargs['uploaded_by_user'] = form.user

                    image = ImageModel(**kwargs)
                    image.save()
                    # saving the image id
                    # alternatively we can store a path to the image via image.get_rendition
                    cleaned_data.update({name: image.pk})
                    print(image)
                    images_list.append(image.pk)
                else:
                    # remove the value from the data
                    del cleaned_data[name]

            elif isinstance(field, FileField):
                document_file_data = cleaned_data[name]
                if document_file_data:
                    DocumentModel = get_document_model()
                    kwargs = {
                        'file': cleaned_data[name],
                        'title': self.get_image_title(cleaned_data[name].name),
                        'collection': self.get_uploaded_image_collection(),
                    }

                    if form.user and not form.user.is_anonymous:
                        kwargs['uploaded_by_user'] = form.user

                    document = DocumentModel(**kwargs)
                    document.save()
                   # print(document)
                    document_list.append(document.pk)
                    cleaned_data.update({name: document.pk})
                else:
                    # remove the value from the data
                    del cleaned_data[name]

        submission = self.get_submission_class().objects.create(
            form_data=form.cleaned_data, # new
            page=self
        )
        #self.send_autoresponder(form)
        #self.send_mail(form,document_list,images_list)
        return submission  

        
        # Use the parent class's method to create the submission
        #return super().process_form_submission(form)
    
    def serve(self, request):
        booking_temp_data = []
        if request.method == 'POST':
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)

            try:
                booking_count = int(request.POST.get('booking_count', 1))
            except ValueError:
                booking_count = 1

            for i in range(1, booking_count + 1):
                form.fields[f'booking_{i}_start_date'] = forms.DateField(
                    label=f"Booking {i} Start Date", #required=True
                )
                form.fields[f'booking_{i}_end_date'] = forms.DateField(
                    label=f"Booking {i} End Date", #required=True
                )
                
                form.fields[f'booking_{i}_frequency_of_booking'] = forms.CharField(
                    label=f"Booking {i} Frequency of Booking", #required=True
                )
                form.fields[f'booking_{i}_start_time'] = forms.CharField(
                    label=f"Booking {i} Start Time", #required=True
                )
                form.fields[f'booking_{i}_finish_time'] = forms.CharField(
                    label=f"Booking {i} Finish Time", #required=True
                )
                form.fields[f'booking_{i}_number_of_participants'] = forms.IntegerField(
                    label=f"Booking {i} Number of Participants", #required=True
                )
                booking = {
                    'start_date': form.data.get(f'booking_{i}_start_date', ''),
                    'end_date': form.data.get(f'booking_{i}_end_date', ''),
                    'frequency_of_booking': form.data.get(f'booking_{i}_frequency_of_booking', ''),
                    'start_time': form.data.get(f'booking_{i}_start_time', ''),
                    'finish_time': form.data.get(f'booking_{i}_finish_time', ''),
                    'number_of_participants': form.data.get(f'booking_{i}_number_of_participants', ''),
                }
                booking_temp_data.append(booking)
            
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
        context['booking_temp_data'] =booking_temp_data
        return TemplateResponse(request, self.get_template(request), context)

    
    class Meta:
        verbose_name = "Facility Hire Form Page"