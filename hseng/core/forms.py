from django import forms
from tinymce.widgets import TinyMCE


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'row': 40}))
