from django.contrib import admin
from myapp .models import upload
# Register your models here.
# admin.site.register(upload)

class uploadAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'file']

admin.site.register(upload, uploadAdmin)
