'''BestHouseSelectionlocked

Professor X is looking to buy a house. Everyone in his family has an opinion on this. His kids demand separate bedrooms, meaning that they need at least 4 bedrooms. He wants no house that is smaller than 2500 square feet. His wife, who keeps the checkbook, sets the budget to be no more than $400,000.

Among the houses that satisfy the above conditions, output information for the two houses that have the lowest ppsf(price per-square-foot) index values.

Input Format

The first line contains one number N, the number of houses.

The next N lines contains 3 integer numbers which are price, number of bedrooms, and square footage.

It is guaranteed that no two houses have the same exact per-square footage price.

Constraints

1 <= N <= 1000

10000 <= price <= 1000000

2 <= number_of_bedrooms <= 6

1000 <= square_footage <= 6000

Output Format

If no house satisfies the conditions, output one line "You are out of luck, Prof.X." (The case and spaces must match.)

If only one house satisfies the conditions, output the price, number of bedrooms, and square footage information of that house.

If two or more houses satisfy the conditions, output two lines, the first containing the house that has the lowest per-square footage price, and the second containing the house that has the second to lowest per-square footage price.

Sample Input 0

6
300000 3 1000
100000 3 2000
600000 5 4000
300000 4 3000
100000 2 3000
300000 5 6000
Sample Output 0

300000 5 6000
300000 4 3000
Explanation 0

House 1 has less than 4 bedrooms.
House 2 has less than 4 bedrooms.
House 3 has price higher than 400000.
House 4 satisfies all conditions, has ppsf of 100.
House 5 has less than 4 bedrooms.
House 6 satisfies all conditions, has ppsf of 50.
Line one of the output has information of House 6.
Line two of the output has information of House 4.'''

















T=int(input())
l=[]
for i in range(T):
    p,b,sqft=map(int,input().split())
    if b>=4 and sqft>=2500 and p<=400000:
        l.append((p,b,sqft))
l.sort(key=lambda x:x[0]//x[2])
if len(l)==1:
    print(*l[0])
elif len(l)>1:
    for i in range(2):
        
           print(*l[i])
else:
    print("You are out of luck, Prof.X.")
