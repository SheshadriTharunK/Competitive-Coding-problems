import math
x=int(input())
n = (math.sqrt(8*x + 1) - 1) / 2
if (n.is_integer()):
    print("YES")
else:
    print("NO")
