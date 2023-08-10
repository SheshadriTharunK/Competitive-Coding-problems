'''TeamLead
A group of N players want to elect a team leader. They each wear a uniform with a distinct ID, and the IDs are in the range of 1 to N.

They decided to use paper ballot to vote for the leader. Each voter writes the ID of a candidate on a ballot and places it in the ballot box. The candidate with the highest number of votes becomes the leader. If two or more candidates have the same number of votes, then the candidate with larger ID will be elected as leader.

Input Format

The first line contains a number N.

The next N lines contains N numbers, which are the N votes. Each number is between 1 and N.

Constraints

1 <= N <= 10^6

Output Format

Output a single line consisting of the winner ID.

Sample Input 0

4
1
1
2
2
Sample Output 0

2'''








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
