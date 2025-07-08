from django.shortcuts import render
from tasks import send_email

# Create your views here.

emil = 'amin138400138400@gmail.com'

send_email.delay(emil)
