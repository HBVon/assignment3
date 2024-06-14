from django.contrib import admin
from .models import TTSlot

class TTSlotAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'module_name', 'teacher_name', 'group_name', 'classroom_name')
    list_filter = ('day', 'module_name', 'teacher_name', 'group_name', 'classroom_name')

admin.site.register(TTSlot, TTSlotAdmin)
