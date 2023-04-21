import math
T=int(input())
Asq_error=0
Bsq_error=0
sumAsq_error=0
sumBsq_error=0
for i in range(T):
    price,b,f1,f2,r1,r2=map(int,input().split())
    AHP = 5000 - 20000*b + 130*f1 + 70*f2 + 30000*r1 + 24000*r2
    BHP = 20000*b + 75*(f1+f2) + 10000*r1 + 5000*r2
    Asq_error=(AHP-price)**2
    Bsq_error=(BHP-price)**2  
    sumAsq_error+=Asq_error 
    sumBsq_error+=Bsq_error 
MeanAsq_error=(sumAsq_error/T)
MeanBsq_error=(sumBsq_error/T)
Armse=math.sqrt(MeanAsq_error)
Brmse=math.sqrt(MeanBsq_error)
print('{:.2f} {:.2f}'.format(Armse,Brmse))
if Armse<=Brmse:
    percent_diff=(Armse/Brmse)*100 
    print("Alice's RMSE is {:.2f}% of Bob's RMSE.".format(percent_diff))
else:
    percent_diff=(Brmse/Armse)*100 
    print("Bob's RMSE is {:.2f}% of Alice's RMSE.".format(percent_diff))
    
