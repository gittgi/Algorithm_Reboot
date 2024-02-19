n = int(input())
arr = list(map(int, input().split()))

max_diff = float("inf")
ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        for k in range(i+1, j+1):
            val = abs(sum(arr[i:k]) - sum(arr[k:j+1]))
            if val < max_diff:
                max_diff = val
                ans = sum(arr[i:j+1])
            elif val == max_diff:
                if ans < sum(arr[i:j+1]):
                    ans = sum(arr[i:j+1])

print(ans)