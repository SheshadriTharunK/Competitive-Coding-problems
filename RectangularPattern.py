h,w=map(int,input().split())
if (h==1 and w==1):
    print("+")
elif (h==1 and w>1):
    print("|",end='')
    for i in range(w-2):
        print("-",end='')
    print("|")
elif (h>1 and w==1):
    print('-',end="\n")
    for i in range(h-2):
            print("|",end='\n')
        
    print("-")
                

elif (h>1 and w>1):
    print("/",end='')
    for j in range(w-2):
            print('-',end='')
    print('\\')
    
    for i in range(h-2):
        print("|", end='')
        print(" "*(w-2), end='')
        #for j in range(w-2):
           # print(" ", end='')
        print("|")
        
    print('\\',end='')
    for j in range(w-2):
            print('-',end='')
    
    print("/")





