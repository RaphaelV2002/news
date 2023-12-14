# blog/admin.py
from django.contrib import admin
from .models import Blog, New

admin.site.register(Blog)
admin.site.register(New)
