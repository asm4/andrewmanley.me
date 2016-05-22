from __future__ import unicode_literals

from django.db.models import Model, TextField, DateTimeField, CharField, \
    EmailField


class EmailMessage(Model):
    """
    This class stores information regarding email messages that are sent
    on this site.
    """
    message = TextField()
    subject = CharField(max_length=128)
    sender = EmailField()
    created = DateTimeField()

    class Meta:
        db_table = 'email_message'
        ordering = ['-created']

    def __unicode__(self):
        return self.sender + ': ' + self.subject
