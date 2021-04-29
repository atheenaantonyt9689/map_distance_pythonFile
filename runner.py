from distance import Mappoint
def run():
    lon1=float(input("enter the longitude:"))
    lat1=float(input("enter the longitude:"))
    lon2=float(input("enter the longitude:"))
    lat2=float(input("enter the longitude:"))

    p1=Mappoint(lon1,lat1)
    p2=Mappoint(lon2,lat2)
    p1.distance(p2)

run()

