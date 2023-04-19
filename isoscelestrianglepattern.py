n=int(input())
if n==1:
    print('+')
if n==2:
    print('','+',end='\n')
    print('+',end='')
    for i in range(1,n):
        print('-',end='')
    print('+')
if n>2:
   k=1
   for i in range(1,n):
      if i==1:
            print(' '*(n-i),end='')
            print('+')
      else:
        print(' '*(n-i),end='')
        print('/',end='')
        print(' '*(2*k-1),end='')
        print("\\")
        k+=1
   print('+',end='')
   print('-'*(2*k-1),end='')
   print('+')
   
   
            
        
        
        