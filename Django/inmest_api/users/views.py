from django.shortcuts import render
from models import IMUser

# Create your views here.

def signup(request):
    user_name = request.POST["user_name"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    phone_number = request.POST["phone_number"]
    password = request.POST["password"]
    
    new_user = IMUser.objects.create(
        user_name = user_name,
        first_name= first_name,
        last_name = last_name,
        phone_number = phone_number
    )
    
    new_user.set_password(password)
    new_user.save()
    