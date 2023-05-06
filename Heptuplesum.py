a=list(map(int,input().split()))
l=[]
sum=0 
for i in range(len(a)):
   
    for j in range(i+1,len(a)):
        
        for k in range(j+1,len(a)):
            
            for s in range(k+1,len(a)):
                
                for m in range(s+1,len(a)):
                   
                    for n in range(m+1,len(a)):
                       
                        for o in range(n+1,len(a)):
                            
                            sum=a[i]+a[j]+a[k]+a[s]+a[m]+a[n]+a[o]
                            if sum==100:
                                print(a[i],a[j],a[k],a[s],a[m],a[n],a[o])
                                exit()
else:
    print("No such heptuple exists!")
                                