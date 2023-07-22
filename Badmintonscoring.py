'''SideOutBadmintonScoringlocked

In old/traditional badminton matches, we use sideout scoring to decide the winner of the match. That means, a player can only score a point when they are serving. If a player serves and wins, they add a point to their score. If a player serves and does not get a point, there is no change to the score, and the serve goes to the other player (who then has a chance to score points). These rules mean it is possible to deduce the score of a game based on the knowledge of who won the various serves, assuming that player A always start serving.

You are now given records of many matches and asked to do the best you can to figure out the status of these matches.

Input Format

The first line will be a positive number, N, indicating the number of input cases. There will then follow N lines. Each line will start with a positive number S (<= 100), indicating the number of serves in the test case. There will then follow S values. Each value will either be the letter A (indicating Palyer A won the point) or the letter B (indicating Player B won the point). Player A always starts out serving.

The game will end the first time the following happens: the player that just scores has score at least 15, and that score is at least 2 higher than the other player. So a game does not end at 15-14, 16-15, and so on, and ends at 15-y (where y <= 13), 16-14, 17-15, etc.

Constraints

1 <= N <= 1000

1 <= S <= 100

Output Format

For each input case, there are two cases.

If the record stops before the match ends, output a line:
Match m: The score is x-y.
Where m is a number denoting the match (starting from 1), and x and y are Player A’s and Player B’s points, respectively, in the current game.

If the match has ended properly because a player has reached 15 points or more and is ahead by at least two points, then output the line:
Match m: Player A/B has won the match with a score of x-y.
(You’ll say which palyer of A and B has won, of course)

Sample Input 0

4
10 A B A A A B B B A A
15 A A A A A A A A A A A A A A A 
4 B A B A
5 B B B A B
Sample Output 0

Match 1: The score is 4-2.
Match 2: Player A has won the match with a score of 15-0. 
Match 3: The score is 0-0.
Match 4: The score is 0-2.
Sample Input 1

9
36 A B A B B A B A B B B A B B B B B A B A B B B A B A B B B B A A B B B B
22 B A B A B A B A B B A B B B B B A A B A A B
13 A B A A B B B B B B B A B
28 A B B B B B B B A B A B A B A B B B B B B B A A B B B B
28 B B B A A B B B B B A B A B B B A A B B B B B A B B B B
28 B A A A B B B B B B B B B B A B B B B A B A B B A B B B
19 A B B B B B B B B B A A B A B A B B A
12 B B B B B B B A B B B B
20 B B B B B B B A A B B B B B B A A B B B
Sample Output 1

Match 1: Player B has won the match with a score of 2-15.
Match 2: The score is 2-5.
Match 3: The score is 2-6.
Match 4: Player B has won the match with a score of 2-15.
Match 5: Player B has won the match with a score of 2-15.
Match 6: Player B has won the match with a score of 2-15.
Match 7: The score is 2-9.
Match 8: The score is 0-9.
Match 9: The score is 2-13.'''


















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
