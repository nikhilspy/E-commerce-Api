from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return  HttpResponse("Features are working Please go to  <button type="submit" value={{excel_path}} onclick="location.href='{% url 'https://github.com/nikhilspy/E-commerce-Api/blob/master/readme.txt' %}'" name='mybtn2'>read.md</button> file to see the Urls ")
