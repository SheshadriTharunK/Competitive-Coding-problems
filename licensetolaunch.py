n = int(input())
space_junk = list(map(int, input().split()))

min_junk = float('inf')
min_day = -1

for i in range(n):
    if space_junk[i] < min_junk:
        min_junk = space_junk[i]
        min_day = i

print(min_day )
