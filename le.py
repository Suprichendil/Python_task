year=2006
if(year % 400 ==0) and (year % 100==0):
    print("{0} is a leap year".format(year))
elif(year % 4 ==0) and (year % 100!=0):
    print("{0} is a leap year".format(year))
else:
    print("{o} is not a leap year".format(year))
