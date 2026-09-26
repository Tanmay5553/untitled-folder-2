import random
import time

def Randomdate(startDate,enddate):
    print("random date between ",startDate,"and",enddate)

    dateformat="%m/%d/%y"
    startTime=time.mktime(time.strptime(startDate,dateformat))
    endTime=time.mktime(time.strptime(enddate,dateformat))

    randomTime=random.random()*(endTime-startTime)
    randomDate=startTime+randomTime
    randomDate=time.strftime(dateformat,time.localtime(randomDate))
    return randomDate

print("randomDate : ",Randomdate("1/1/26","12/12/26"))