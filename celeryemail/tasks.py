from celery import shared_task
from send_email.celery import app
from django.core.mail import send_mail


@shared_task
def mail():
    send_mail(
        subject='Celery is Working!', 
        message='This is a proof message that celery is working',
        from_email='',                                                          #from email
        recipient_list=[''],                                              #To the sending email
        fail_silently=True
        )
    return None