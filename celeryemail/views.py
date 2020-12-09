from django.shortcuts import HttpResponse, render
from .tasks import mail
from .models import User
from django.contrib import messages
from tablib import Dataset


# Create your views here.

def index(request):
    mail.delay()
    return HttpResponse("<h1>Go to excel!!</h1>")


def simple_upload(request):
    if request.method == 'POST':
        dataset =  Dataset()
        new_user = request.FILES['myfile']

        if not new_user.name.endswith('xlsx'):
            messages.info(request,'Wrong Format')
            return render(request,'excel.html')

        imported_data = dataset.load(new_user.read(),format='xlsx')
        for data in imported_data:
            value = User(
                data[0],
                data[1],
                data[2],
                data[3]
            )
            value.save()
    return render(request,'excel.html')