import requests
from math import sin, cos, sqrt, atan2,radians

requests.packages.urllib3.disable_warnings()

res = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address=IIT+powai")
r=res.json()

lat_r = r["results"][0]["geometry"]["location"]["lat"]
lng_r = r["results"][0]["geometry"]["location"]["lng"]


def distance(lat1,lng1,lat2,lng2):
 R = 6373.0

 lat_1 = radians(lat1)
 lon_1 = radians(lng1)
 lat_2 = radians(lat2)
 lon_2 = radians(lng2)

 dlon = lon_2 - lon_1
 dlat = lat_2 - lat_1
 a = (sin(dlat/2))**2 + cos(lat_1) * cos(lat_2) * (sin(dlon/2))**2
 c = 2 * atan2(sqrt(a), sqrt(1-a))
 dist = R * c

 return dist 




f = open("input.txt",'r')                    #opening file
count =0
lines =f.readlines()
f.close()

f = open("input.txt",'r')                    #making a copy the file as a list 
lis =f.readlines()
f.close()

for i in range(len(lines)):                  #removing new line characters    
 lines[i] = lines[i].rstrip()

for i in range(len(lis)):
 lis[i] = lis[i].rstrip() 
                         
for i in lis:                                #correcting for blank characters at the end of file 
 if(i)=='':                                   
  count=count+1

for i in range(len(lines)):                  #adding '+' in space between words
 a=list(lines[i])
 for j in range(len(lines[i])):
  if(a[j]==' '):
   a[j]='+'
 lines[i]="".join(a) 

dist_array={}
                                             #print lis just for debugging
                                             #print len(lis)
for i in range(len(lis)-count):              #correcting for blank lines if any at the end of file
 res = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address="+lines[i])
 r = res.json()
 if(r["status"]!="ZERO_RESULTS"):
  dist_array[lis[i]]=distance(r["results"][0]["geometry"]["location"]["lat"],r["results"][0]["geometry"]["location"]["lng"],lat_r,lng_r)
 elif(r["status"]=="ZERO_RESULTS"): 
  dist_array[lis[i]]=1100000 

for key,value in sorted(dist_array.iteritems(), key=lambda (k,v): (v,k)): #list of sorted places
 print "%s:%s km" % (key,value)
