def plusMinus(arr,count1,count2,count3):
    count1=0
    count2=0 
    count3=0 
    for i in range(len(arr)):
       if arr[i]>=1:
          count1+=1 
       elif arr[i]<0:
          count2+=1 
       else:
        count3+=1

    p1=count1/n
    p2=count2/n 
    p3=count3/n 
    print('{:.6f}'.format(p1)) 
    print('{:.6f}'.format(p2)) 
    print('{:.6f}'.format(p3)) 
        
        
    
    
    
    
    
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    count1=0
    count2=0 
    count3=0
    plusMinus(arr,count1,count2,count3)
