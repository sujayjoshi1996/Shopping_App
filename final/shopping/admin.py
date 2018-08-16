from django.contrib import admin
from .models import profile,userStripe,data

# Register your models here.
admin.site.register(profile)
admin.site.register(userStripe)
admin.site.register(data)
