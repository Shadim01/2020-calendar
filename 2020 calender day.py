# 2020 calender Date
January=[0,'wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri']
Ferbruary=[0,'sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat']
March=[0,'sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue']
April=[0,'wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu']
May=[0,'fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun']
June=[0,'mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue']
July=[0,'wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri']
August=[0,'sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat']
September=[0,'thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','tue','wed']
october=[0,'thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat']
November=[0,'sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon']
December=[0,'tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu']
print('''
1=January
2=Ferbruary
3=March
4=April
5=May
6=June
7=July
8=August
9=September
10=october
11=November
12=December
''')
Month=int(input('Enter Your Month: '))
Date=int(input('Enter Your Date: '))
if Month==1:
    print(January[Date])
elif Month==2:
    print(Ferbruary[Date])
elif Month==3:
    print(March[Date])
elif Month==4:
    print(April[Date])
elif Month==5:
    print(May[Date])  
elif Month==6:
    print(June[Date])
elif Month==7:
    print(July[Date])
elif Month==8:
    print(August[Date])
elif Month==9:
    print(September[Date]) 
elif Month==10:
    print(october[Date]) 
elif Month==11:
    print(November[Date])  
elif Month==2:
    print(December[Date])   
else:
    print('Try Again')