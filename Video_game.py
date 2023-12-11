def find(n,c):
    a1=0 
    a2=sum(c)-1
    if a2==1 :
        return 0
    for i in range(n):
        if c[i]==0:
            a1-=1 
            
        else: 
           a1+=c[i]
        a2-=1 
        if a1>a2: 
            return i+1
def main():
    n=int(input())
    c=[]
    for i in range(n):
        k=int(input())
        c.append(k)
    print(find(n,c))
main()
