T=int(input())
sum1=0 
sum2=0
count1=0
count2=0
for i in range(T):
    a,b,c=map(int,input().split())
    if (b<=3):
        count1+=1 
        sum1+=c
    elif(b>=4):
        count2+=1 
        sum2+=c 
print(sum1//count1,sum2//count2)