
import psycopg2 as ps
import pandas as pd
import warnings
from geopy.geocoders import Nominatim
import numpy as np
class Search():
    def __init__(self,array,element):
        self.array=array
        self.element=element
    def ternary_search(self):
        self.array=list(map(int,self.array.split()))
        l=0
        r=len(self.array)-1
        while l<=r:
            m1=l+(r-l)//3
            m2=r-(r-l)//3
            if self.array[m1]==int(self.element):
                return m1
            elif self.array[m2]==self.element:
                return m2
            elif self.array[m1]<self.element<self.array[m2]:
                l=m1+1
                r=m2-1
            elif self.element<self.array[m1]:
                r=m1-1
            elif self.element>self.array[m2]:
                l=m2+1
        return ('there is no such element')

if __name__=='__main__':

    conn = ps.connect(host="127.0.0.1", port = 5432, database="search", user="postgres", password="123456", options="-c search_path=bookings")
    aparts = pd.read_sql("SELECT * FROM public.sort_sort", con=conn).drop('id',axis=1).iloc[-1,:]
    a=Search(aparts[0],aparts[1])
    ans=a.ternary_search()
    