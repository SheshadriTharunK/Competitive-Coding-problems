a=input()
dict1 = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30,12:31}
dict2={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',0:'Sunday'}
days = 0
year,month,day=map(int,a.split(':'))
for i in range(1,month):
    if i==2:
        if year%4==0 and (year%100!=0 or year%400==0):
            days+=29 
        else:
            days+=28 
    else:
        days+=dict1[i]
else:
    days+=day 
week=days%7 
print(dict2[week])

            