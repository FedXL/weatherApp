from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', start, name='start_page')
]