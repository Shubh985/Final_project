# from _future_ import unicode_literals
from django.shortcuts import render

#create your view here

def signup_view(request):
    return render(request,'signup.html')

# login view

def login_view(request):
    return render(request,'login.html')
