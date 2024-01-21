from django.contrib import admin
from .models import Company,UserData, Contact, Prediction
# Register your models here.
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'telefonnummer']

class PostAdmin(admin.ModelAdmin):
    list_display = ['image']
    list_filter = ['image']
    search_fields = ['image']

class ContactDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(Company)
admin.site.register(Prediction,PostAdmin)
admin.site.register(UserData,UserDataAdmin)
admin.site.register(Contact,ContactDataAdmin)