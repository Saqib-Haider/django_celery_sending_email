from django.shortcuts import HttpResponse
from .tasks import mail
# Create your views here.

def index(request):
    mail.delay()
    return HttpResponse("<h1>Email has been sent!!</h1>")