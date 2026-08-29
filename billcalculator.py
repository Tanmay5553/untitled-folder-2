def totalamt( billamt,tipamt):
    totalbill=billamt*(1+0.01*tipamt)
    totalbill=round(totalbill,2)
    print("total bill is",totalbill)

totalamt(1500,120)
