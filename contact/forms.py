from django.forms import ModelForm, EmailInput, TextInput, Textarea

from contact.models import EmailMessage


class EmailMessageForm(ModelForm):
    """
    This class is used to create a form based on the EmailMessage model.
    """
    class Meta:
        model = EmailMessage
        fields = ['sender', 'subject', 'message']
        widgets = {
            'sender': EmailInput(attrs={'class': 'form-control',
                                        'required': 'true'}),
            'subject': TextInput(attrs={'class': 'form-control',
                                        'required': 'true'}),
            'message': Textarea(attrs={'class': 'form-control',
                                       'required': 'true'}),
        }
