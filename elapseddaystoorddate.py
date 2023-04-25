n=int(input())
year=2000 
days=366 
while(n>=days):
    n=n-days 
    year=year+1 
    if year%4==0 and (year%100!=0 or year%400==0):
        days=366 
    else:
        days=365 
print(year,n+1)
    