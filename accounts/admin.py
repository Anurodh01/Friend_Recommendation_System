from django.contrib import admin
from .models import *
# Register your models here.

from .models import user
admin.site.register(user)

admin.site.register(UData)