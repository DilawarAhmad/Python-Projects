from django.shortcuts import render
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.
def index(request):
    return render('templates/index.html')
