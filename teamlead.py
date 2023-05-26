l={}
N=int(input())
for i in range(N):
    x=int(input())
    if x in l:
        l[x]+=1 
    else:
        l[x]=1 
max_count=0
id_win=0 
for id,count in l.items():
    if count>max_count or (count==max_count and id>id_win):
        max_count=count 
        id_win=id 
print(id_win)