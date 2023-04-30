n=int(input())
if n<60:
    print('{} Seconds'.format(n))
elif n>=60 and n<3600:
    minutes=n//60
    seconds=n%60
    if (seconds)>0:
        print('{} Minutes {} Seconds'.format(minutes,seconds))
    else:
        print('{} Minutes'.format(minutes))
elif n>= 3600 and n<86400:
    hours=n//3600 
    minutes=(n%3600)//60 
    seconds=n%60 
    if(seconds):
         print('{} Hours {} Minutes {} Seconds'.format(hours,minutes,seconds))
    elif (minutes):
        print('{} Hours {} Minutes.format'.format(hours,minutes,seconds))
    elif(hours):
       print('{} Hours'.format(hours))
elif n>=86400:
    days=n//86400
    hours=(n%86400)//3600
    minutes=(n%3600)//60 
    seconds=n%60
    if(seconds):
         print('{} Days {} Hours {} Minutes {} Seconds'.format(days,hours,minutes,seconds))
    elif (minutes):
        print('{} Days {} Hours {} Minutes'.format(days,hours,minutes))
    elif(hours):
        print('{} Days {} Hours'.format(days,hours))
    elif(days):
        print('{} Days'.format(days))
        
    
    