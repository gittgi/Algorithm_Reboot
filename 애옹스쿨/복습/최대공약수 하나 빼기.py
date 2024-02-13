import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def get_gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        x, y = y, x % y
    return y

prefix = [0] * n
prefix[0] = arr[0]
suffix = [0] * n
suffix[-1] = arr[-1]

for i in range(1, n):
    prefix[i] = get_gcd(prefix[i-1],arr[i])

for i in range(n-2, -1, -1):
    suffix[i] = get_gcd(suffix[i+1], arr[i])

max_val = -1
idx = -1
for i in range(n):
    if i == 0:
        if arr[i] % suffix[i+1] != 0:
            if max_val < suffix[i+1]:
                max_val = suffix[i+1]
                idx = i

        
    elif i == n-1:
        if arr[i] % prefix[i-1] != 0:
            max_val = max(prefix[i-1], max_val)
            if max_val < prefix[i-1]:
                max_val = prefix[i-1]
                idx = i
    
    else:
        if prefix[i-1] == suffix[i+1] and arr[i] % prefix[i-1]:
            if max_val < prefix[i-1]:
                max_val = prefix[i-1]
                idx = i

if idx == -1:
    print(-1)
else:
    print(max_val, arr[idx])

