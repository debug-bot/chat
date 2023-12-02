from django.contrib import admin
from .models import *

admin.site.register(Chat)
admin.site.register(Prompt)
admin.site.register(Response)
admin.site.register(File)
admin.site.register(Settings)
admin.site.register(Profile)


