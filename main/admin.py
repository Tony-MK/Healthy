from django.contrib import admin

# Register your models here.
from .models import *

# User Types
admin.site.register(Parent);
admin.site.register(CareTaker);
#admin.site.register(Child);


admin.site.register(Gig);







