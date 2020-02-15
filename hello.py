#print("hello world")

date=int(input("enter the date between 1 to 30"))
if date>31:
    print("invalid input")
else:
    rem=date % 7
    print (rem)
    if rem==1:
        print("%d is Sunday" %date)
    elif rem==2:
        print(" %d is monday" %date)
    elif rem==3:
        print(" %d is Tuesday" %date)
    elif rem==4:
        print(" %d is Wednesday" %date)
    elif rem==5:
        print(" %d is Thrusday" %date)
    elif rem==6:
        print(" %d is Friday" %date)
    else: 
        print(" %d is Saturday" %date)