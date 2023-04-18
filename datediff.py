start=list(map(int,input().split(':')))
end=list(map(int,input().split(':')))
dict1={1:31,3:31,4:30,5:31,6:30,7:31}
k1=365 
k2=366 
days=0
for i in range(start[0],end[0]):
    if i%4==0 and i%100!=0 or i%400==0:
        days+=366 
    else:
        days+=365 
for i in range(start[1],end[1]):
    if i==2 and (start[1]%4==0 and start[1]%100!=0 or start[1]%400==0):
        days+=29 
         
    elif i==2:
        days+=28 
    else:
        days+=dict1[i]
print(days)
        
