from datetime import date,time,datetime

today= date.today()
now=datetime.now()

print("today's date is :",today)
print("current time is: ",now)

print("use data component")
print(today.day,"-",today.month,"-",today.year)