from django.contrib import admin
from licenses.models import Client, License
# Register your models here.
admin.site.register(License)
admin.site.register(Client)
