def binary_search(N, k):
    start = 1
    end = N*N

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in range(1, N+1):
            count += min(mid // i, N)
        
        if count < k:
            start = mid + 1

        else:
            end = mid - 1

    return start

N = int(input())
k = int(input())

print(binary_search(N, k))