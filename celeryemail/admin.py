from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class UserAdmin(ImportExportModelAdmin):
    list_display = ('name','email','company')
admin.site.register(User)
