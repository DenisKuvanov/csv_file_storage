from django.contrib import admin

from storage_app.models import CSV_file


# Register your models here.
@admin.register(CSV_file)
class CSV_fileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'owner', 'file', 'created_at']
