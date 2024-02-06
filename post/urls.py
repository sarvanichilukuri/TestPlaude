from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index, name = 'index'),
    path('fetchData/',extract_and_save_data, name = 'extract_and_save_data')
]

