from django.core.mail import EmailMessage
from django.conf import settings


def send_email(subject, message, to, content_type=None):
    """
s       end_email parameters: Subject, Message, To
    """
    try:
        msg = EmailMessage(
            subject, message, settings.EMAIL_FROM, to)

        if content_type is not None:
            msg.content_subtype = content_type
        msg.send()
    except Exception as e:
        print('exceptions is ', e)
        raise Exception('Error in sending email.', e)
