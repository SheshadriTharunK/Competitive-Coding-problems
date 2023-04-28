time,am_pm=input().split(' ')
hours,minutes,seconds=map(int,time.split(':'))
if hours==12 and am_pm=='am':
    hours=0 
elif hours<12 and am_pm=='pm':
    hours+=12 
seconds=hours*3600+minutes*60+seconds 
print(seconds)
