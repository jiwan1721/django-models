from django.contrib import admin

# Register your models here.
from .models import Modeltry  # importing Modeltry class from models.py

#to register class we have to write code for admin
admin.site.register(Modeltry)  #it will show the model to admin site