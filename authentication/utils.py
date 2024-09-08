from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user):
    verification_code = user.verification_code
    subject = 'Verify your email'
    message = f'Your verification code is {verification_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
