
def marsExploration(s):
    i=0
    k='SOS'
    count=0
    while(i<len(s)):
        if s[i]!=k[0]:
            count+=1
        if i+1<len(s) and s[i+1]!=k[1]:
            count+=1 
        if i+2<len(s) and s[i+2]!=k[2]:
             count+=1
        i=i+3
    print(count)
        
if __name__ == '__main__':
    
    s = input().upper().strip()

    marsExploration(s)
