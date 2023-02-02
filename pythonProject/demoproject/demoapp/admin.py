from django.contrib import admin
from .models import folder


# Register your models here.
class FolderForm(admin.ModelAdmin):
    list_display = ['language', 'upload']


admin.site.register(folder)
