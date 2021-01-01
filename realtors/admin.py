from django.contrib import admin
from .models import Realtors
# Register your models here

class RealtorsAdmin(admin.ModelAdmin):
    list_display = ('name','id','email','hire_date')
    list_display_links = ('name','id')




admin.site.register(Realtors,RealtorsAdmin)