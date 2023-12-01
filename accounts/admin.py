from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Prompt)
admin.site.register(Response)

