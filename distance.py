
import math
class Mappoint:
    R=6731
    def __init__(self,longitude,latitude):       
        self.longitude=longitude
        self.latitude=latitude
    def distance(self,p2):       
        dlon=p2.longitude-self.longitude
        dlat=p2.latitude-self.latitude
        print("dlon:",dlon)
        print("dlat:",dlat)
        a = (math.sin(dlat/2))**2 + math.cos(self.longitude) *math.cos(p2.latitude) * (math.sin(dlon/2))**2

        print("aaa:",a)
        c = 2* math.atan2((a)**0.5,(1-a)**0.5 )
        print("c",c)
        d= Mappoint.R*c
        print("distance:",d)   
               
"""lon1=int(input("enter the longitude1:"))
lat1=int(input("enter the latitude 1"))
lon2=int(input("enter the longitude2:"))
lat2=int(input("enter the latitude2:"))

p1=Mappoint(lon1,lat1)
p2=Mappoint(lon2,lat2)
p1.distance(p2)"""
