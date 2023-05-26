s=input()
a={}
oddexists=False
sum=0
for i in s:
    if i not in a:
        a[i]=1 
    else:
        a[i]+=1 
for i in a:
     if a[i]%2==0:
          sum+=a[i]
     elif a[i]%2!=0:
           sum+=a[i]-1
           oddexists=True 
if(oddexists):
    sum+=1
            
 
print(sum)