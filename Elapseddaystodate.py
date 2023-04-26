start_date=(2020,1,1)
year1,month1,day=start_date 
days=int(input())
for i in range(days):
    day+=1 
    if month1 in [1,3,5,7,8,10]:
        if day>31:
            day=1
            month1+=1 
    elif month1 in [4,6,9,11]:
        if day>30:
            day=1
            month1+=1 
    else:
        if year1%4==0 and (year1%100!=0 or year1%400==0):
            if day>29:
                day=1
                month1+=1
        else:
            if day>28:
                day=1
                month1+=1 
    if month1>12:
        month1=1
        year1+=1 
print('{:02d}:{:02d}:{:02d}'.format(year1,month1,day))
    
    