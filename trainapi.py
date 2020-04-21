import os as os
import sys as sys
import pickle as pickle
import requests as requests
import json as json
import random as random
import string as string
import numpy as np

assert sys.version_info >= (3, 0), "Must run with Python 3"

apiloc = "https://api.rtt.io/api/v1/json/search/"

def loadauth(loginfile='auth.txt'):
    with open(loginfile, "r") as f:
        userpass = f.readlines()
        username = userpass[0][:-1]  # need to strip \n character
        password = userpass[1][:-1]
    return (username,password)


def requestwrapper(reqstr):
    req = requests.get(reqstr,auth=authpair)
    if req.status_code == 200:
        return req.json()
    else:
        print("Error in request, %d"%req.status_code)
        return

def getstation(station):
    #Get station data for now
    return requestwrapper(apiloc+station)

def getstationpair(stationa,stationb):
    #Get station to station data
    return requestwrapper(apiloc+stationa+'/to/'+stationb)

def getstationpairdate(stationa,stationb,date):
    #Get station to station data for specific date
    assert len(date) == 10, "Date must be of format 2010/01/01"
    return requestwrapper(apiloc+stationa+'/to/'+stationb+'/'+date)

def getstationdate(station,date):
    #Get station data for specific date
    assert len(date) == 10, "Date must be of format 2010/01/01"
    return requestwrapper(apiloc+station+'/'+date)


authpair = loadauth()

