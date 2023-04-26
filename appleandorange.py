
def countApplesAndOranges(s, t, a, b,m,n):
    da=list(map(int,input().split()))
    db=list(map(int,input().split()))
    ad=[]
    od=[]
    count1=0 
    count2=0 
    for i in range(len(da)):
        k=da[i]+a 
        ad.append(k)
    for i in range(len(db)):
        k=db[i]+b
        od.append(k)
    for i in ad:
        if i in range(s,t+1):
            count1+=1
    for i in od:
        if i in range(s,t+1):
            count2+=1
    print(count1)
    print(count2)
    
if __name__ == '__main__':
    s,t=map(int,input().split())
    a,b=map(int,input().split())
    m,n=map(int,input().split())
    
    

    countApplesAndOranges(s, t, a, b,m,n)
