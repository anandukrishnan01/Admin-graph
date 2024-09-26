# admin.py

from django.contrib import admin
from .models import DataEntry

class DataEntryAdmin(admin.ModelAdmin):
    list_display = ('category', 'value')
    
    change_list_template = 'admin/report_app/dataentry_change_list.html'

    def changelist_view(self, request, extra_context=None):
        # Add custom context data here if needed
        extra_context = extra_context or {}
        # Fetch data for the graph
        data = DataEntry.objects.all()
        extra_context['data'] = data
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(DataEntry, DataEntryAdmin)
