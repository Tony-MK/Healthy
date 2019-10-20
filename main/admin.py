from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User,Child,CareTaker

admin.site.register(User);
admin.site.register(Child);
admin.site.register(CareTaker);





