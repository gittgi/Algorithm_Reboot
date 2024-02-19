n = int(input())
arr = list(map(int, input().split()))
ans_diff = float("inf")
ans_total = 0

for p in range(1, n):
    s = 0
    e = n - 1
    max_diff = float("inf")
    total = 0
    left = sum(arr[s:p])
    right = sum(arr[p:e+1])
    while s < p and p <= e:
        if abs(left - right) < max_diff:
            max_diff = abs(left - right)
            total = left+right
         
        
        if left < right:
            right -= arr[e]
            e -= 1
        elif left > right:
            left -= arr[s]
            s += 1
        else:
            break
    
    if ans_diff > max_diff:

        ans_diff = max_diff
        ans_total = total
    elif ans_diff == max_diff:

        if ans_total < total:

            ans_total = total

print(ans_total)


