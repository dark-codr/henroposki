import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import BadHeaderError, EmailMessage, send_mail, send_mass_mail
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .forms import ContactForm


# Create your views here.
def home_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            # html_message = render_to_string('emails/core/support_email.html', {'message': message, 'from_email': from_email, 'subject': subject})

            try:
                send_mail(
                    subject, 
                    message, 
                    from_email, 
                    ['info@hsengineering.com'], 
                    # html_message=html_message, 
                    fail_silently=False
                    )
                messages.success(request, "Your Email Has been sent successfuly")
            except BadHeaderError:
                messages.error(request, "There was an error sending yout email at the moment, please try again later.")
                # return HttpResponse('Invalid Header found')
            return redirect('home')
    return render(request, 'pages/home.html', {'form': form})
