from andrewmanley import settings
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EmailMessageForm
from .models import EmailMessage


def index(request):
    """
    Returns a contact form or processes the form.
    """
    if request.method == 'POST':
        form = EmailMessageForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email = EmailMessage()
            email.sender = sender
            email.subject = subject
            email.message = message
            email.created = datetime.now()

            try:
                email.save()

                recipients = settings.EMAIL_RECEIVERS
                send_mail('AndrewManley.me - ' + subject, message, sender,
                          recipients)
            except Exception as e:
                messages.error(request, 'Error sending message.')
                messages.error(request, str(e))
                return HttpResponseRedirect('/contact/thanks/')

            messages.success(request, 'Your email has been sent!')
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = EmailMessageForm()
    return render(request, 'contact/index.html', {'form': form})


def contact_thanks(request):
    """
    Returns a page to thank the user for the email.
    """
    return render(request, 'contact/thanks.html', {})
