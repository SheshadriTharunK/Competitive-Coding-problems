A=[]
B=[]
T=int(input())

for i in range(T):
    price, b, f1, f2, r1, r2=map(int,input().split()) 
    AP=5000 - 20000*b + 130*f1 + 70*f2 + 30000*r1 + 24000*r2
    BP=20000*b + 75*(f1+f2) + 10000*r1 + 5000*r2 
    Aabs=abs(AP-price)
    Babs=abs(BP-price)
    A.append(Aabs)
    B.append(Babs)
A.sort(reverse=True)
B.sort(reverse=True)
A=A[2:]
B=B[2:]
sum_A=sum(A)
sum_B=sum(B)
MAA=sum_A/(T-2)
MAB=sum_B/(T-2)
print('{:.2f} {:.2f}'.format(MAA,MAB))
per_A=(MAA/MAB)*100
per_B=(MAB/MAA)*100
if MAA<=MAB:
    print("Alice's MAE is {:.2f}% of Bob's MAE.".format(per_A))
else:   
    print("Bob's MAE is {:.2f}% of Alice's MAE.".format(per_B))