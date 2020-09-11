from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return  HttpResponse("Features are working Please go to read.md file to see the Urls ")
