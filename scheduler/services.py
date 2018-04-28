from django.core.mail import send_mail, EmailMessage
from Constants import EMAIL

def create_email(data):
    mail = EmailMessage(
        subject= data.get(EMAIL.SUBJECT) if data.get(EMAIL.SUBJECT) != None else EMAIL.DEFAULT_SUBJECT,
        body= data.get(EMAIL.BODY) if data.get(EMAIL.BODY) != None else EMAIL.DEFAULT_BODY,
        from_email = data.get(EMAIL.FROM) if data.get(EMAIL.FROM) != None else EMAIL.DEFAULT_FROM,
        to = data.get(EMAIL.RECIPIENT_LIST) if data.get(EMAIL.RECIPIENT_LIST) != None else EMAIL.DEFAULT_RECIPIENT_LIST,
        bcc= data.get(EMAIL.BCC) if data.get(EMAIL.BCC) != None else EMAIL.BCC,
    )
    return mail

def SendEmail(data):
    mail = create_email(data)
    mail.send()


