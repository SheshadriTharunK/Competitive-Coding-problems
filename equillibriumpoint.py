def equilibriumPoint(A, n):
    if n == 1:
        return 1
    total_sum = sum(A)
    left_sum = 0
    for i in range(n):
        if left_sum == total_sum - left_sum - A[i]:
            return i + 1
        left_sum += A[i]
    return -1
