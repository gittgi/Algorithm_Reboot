import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

ans = 0
min_val = float("inf")

for i in range(n-1):
    for j in range(i+1, n):
        
        total = prefix[j+1] - prefix[i]
        s = i
        e = j - 1

        while s <= e:
            mid = (s + e) // 2
            half = prefix[mid+1] - prefix[i]

            if abs(half - total + half) < min_val:
                ans = total

                min_val = abs(half - total + half)
            elif abs(half - total + half) == min_val:
                if total > ans:
                    ans = total
     
            
            if total - half == half:
                break
            elif total - half > half:
                s = mid + 1
            else:
                e = mid - 1
                

print(ans)