from django.contrib import admin
from BRMSapp.models import book

# Register your models here.
class testAdmin(admin.ModelAdmin):
    list_display=['title']
    


admin.site.register(book,testAdmin)