from django.contrib import admin
from .models import Class

class ClassAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('class_name', 'slug', 'class_description', 'class_start_date','class_end_date', 'modified')

admin.site.register(Class)

# Register your models here.
