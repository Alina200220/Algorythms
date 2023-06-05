from django.urls import path
from .views import *

urlpatterns = [
    path('search/', SortView.as_view()), 
    path('search/get', SortListCreate.as_view()), 
]