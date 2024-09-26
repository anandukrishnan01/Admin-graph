# views.py

from django.http import JsonResponse
from django.shortcuts import render
from .models import DataEntry

def pie_chart(request):
    data_entries = DataEntry.objects.all()
    labels = [entry.category for entry in data_entries]
    values = [entry.value for entry in data_entries]
    return render(request, 'piechart.html', {'labels': labels, 'values': values})


def get_data_entries(request):
    data_entries = DataEntry.objects.all()
    data = {'entries': [{'category': entry.category, 'value': entry.value} for entry in data_entries]}
    print("bllahhh")
    print("data",data)
    return JsonResponse({'entries': data})