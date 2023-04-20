l=input().split()
sum=0
a=int(max(l))
b=int(min(l))
for i in l:
    sum+=int(i)
print(sum-(a+b))

