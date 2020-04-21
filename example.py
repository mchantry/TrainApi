import trainapi
req = trainapi.getstationpairdate("KGX","CBG","2020/06/14")
#There's loads of data in here, a combination of dictionaries and lists
#Printing the object will help illuminate but here's an example
print("Serices from KGX to CBG")
for serv in req['services']:
    ori_time = serv['locationDetail']['origin'][0]['publicTime']
    dep_time = serv['locationDetail']['destination'][0]['publicTime']
    print("Departs %s, arrives %s"%(ori_time,dep_time))
