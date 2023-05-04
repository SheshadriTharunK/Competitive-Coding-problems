T=int(input())
for i in range(T):
    A=0 
    B=0
    s=input().split()
    k=s[1:]
    if k[0]=='A':
        A+=1 
    for a in range(1,len(k)):
       if k[a-1]==k[a]:
            if k[a-1]=='A':
                A+=1 
            elif k[a-1]=='B':
                B+=1
            if (A>=15) and (A-B>=2):
                break 
            elif (B>=15) and (B-A>=2):
                break
    if (A>=15 and A-B>=2):
            print("Match {}: Player A has won the match with a score of {}-{}.".format(i+1,A,B))
    elif (B>=15 and B-A>=2):
            print("Match {}: Player B has won the match with a score of {}-{}.".format(i+1,A,B))
    else:
              print("Match {}: The score is {}-{}.".format(i+1,A,B))
