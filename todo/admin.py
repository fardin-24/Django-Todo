from django.contrib import admin
from .models import Tasks
# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')
    search_fields = ('task',)

admin.site.register(Tasks,TasksAdmin)

