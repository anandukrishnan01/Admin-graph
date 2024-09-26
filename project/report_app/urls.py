from django.urls import path
from .views import get_data_entries, pie_chart
urlpatterns = [
    # Other URL patterns
     path('pie/', pie_chart, name='piechart'),  
    path('admin/get_data_entries/', get_data_entries, name='get_data_entries'),

]
