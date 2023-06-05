from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.response import Response
from yaml import serialize

import back.sort as sort


from .models import Sort
from .serializers import SortSerializer
from rest_framework import generics

import psycopg2 as ps
import pandas as pd
import warnings
from geopy.geocoders import Nominatim
import numpy as np

class SortListCreate(generics.ListCreateAPIView):
      queryset = Sort.objects.all()
      serializer_class = SortSerializer

class SortView(APIView):
    
    def get(self, request):
        aparts = Sort.objects.all()
        serializer = SortSerializer(aparts, many=True)
        conn = ps.connect(host="127.0.0.1", port = 5432, database="search", user="postgres", password="123456", options="-c search_path=bookings")
        arr = pd.read_sql("SELECT * FROM public.sort_sort", con=conn).drop('id',axis=1).iloc[-1,:]
        a=sort.Search(arr[0],arr[1])
        ans=a.ternary_search()
        return Response(ans)
       
            
    def post(self, request):
        serializer = SortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
