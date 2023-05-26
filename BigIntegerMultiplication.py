n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = [0] * (n + m)
for i in range(m):
    carry = 0
    for j in range(n):
        product = a[n - 1 - j] * b[m - 1 - i] + carry
        carry = product // 10
        digit = product % 10
        result[n + m - i - j - 1] += digit

    result[n + m - i - n - 1] += carry
for i in range(len(result)):
    if result[i]==0:
        continue 
    else:
        print(result[i],end=' ')



