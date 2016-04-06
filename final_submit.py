
import requests
requests.packages.urllib3.disable_warnings() # cause my system has some problem. also the program runs a bit slow, could not figure out why

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
 res = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+lines[i]+'&destination=IIT+Powai')
 r = res.json()
 if(r["status"]!="ZERO_RESULTS"):
   dist_array[lis[i]]= r["routes"][0]["legs"][0]["distance"]["text"]
 elif(r["status"]=="ZERO_RESULTS"):
   dist_array[lis[i]]="1100000 km"                                       #assigning arbit large value if place not found

   

for key in dist_array:                                                   #converting the distance in appropriate data type for sorting
 x=(dist_array[key].rstrip(" km"))
 dist_array[key]=float(x.replace(",",''))

for key,value in sorted(dist_array.iteritems(), key=lambda (k,v): (v,k)): #list of sorted places
 print "%s" % (key)










