from django.contrib import admin
from .models import *

# Register your models here.
class OnlineAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'course')
admin.site.register(OnlineForm, OnlineAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'messagetext')
admin.site.register(Contact, ContactAdmin)