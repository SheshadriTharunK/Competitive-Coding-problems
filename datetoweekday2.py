year2,month2,day2=map(int,input().split(':'))
days=0
dict1={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dict2={3:'Monday',4:'Tuesday',5:'Wednesday',6:'Thursday',0:'Friday',1:'Saturday',2:'Sunday'}
for i in range(2000,year2):
    if i%4==0 and (i%100!=0 or i%400==0):
        days+=366 
    else:
        days+=365 
for i in range(1,month2):
    if i==2:
        if year2%4==0 and (year2%100!=0 or year2%400==0):
            days+=29 
        else:
            days+=28 
    else:
        days+=dict1[i]
days+=day2 

week=days%7 
print(dict2[week])
    
    