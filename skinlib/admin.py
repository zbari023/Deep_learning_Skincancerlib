from django.contrib import admin
from .models import Image

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['image']
    list_filter = ['image']
    search_fields = ['image']
    

admin.site.register(Image ,PostAdmin) 