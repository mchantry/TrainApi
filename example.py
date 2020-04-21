import trainapi
req = trainapi.getstationpairdate("KGX","CBG","2020/06/14")
#There's loads of data in here, a combination of dictionaries and lists
#Printing the object will help illuminate but here's an example
print("Services from KGX to CBG")
for serv in req['services']:
    toc = serv['atocName']
    ori_time = serv['locationDetail']['origin'][0]['publicTime']
    dep_time = serv['locationDetail']['destination'][0]['publicTime']
    print("%s service, departs %s, arrives %s"%(toc,ori_time,dep_time))
