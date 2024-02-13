import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

prefix = [0] * (n+1)
suffix = [0] * (n+1)

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

for i in range(n-1, -1, -1):
    suffix[i] = suffix[i+1] + arr[i]



min_val = float("inf")
ans = 0
# i -> s~i, i+1 ~ e 까지
for i in range(n-1):
    s = 0
    e = n-1
    while s <= i and i < e:
  
        diff = abs((prefix[i+1] - prefix[s]) - (suffix[i+1]- suffix[e+1]))
     
        if diff < min_val:
            min_val = diff
            ans = prefix[e+1] - prefix[s]
         

        elif diff == min_val:
            if prefix[e+1] - prefix[s] > ans:
                ans = prefix[e+1] - prefix[s]
        
        if (prefix[i+1] - prefix[s]) > suffix[i+1]- suffix[e+1]:
            s += 1
        elif (prefix[i+1] - prefix[s]) < suffix[i+1]- suffix[e+1]:
            e -= 1
        else:
            break

print(ans)