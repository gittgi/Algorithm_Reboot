import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))


prefix = [0] * (w+2)
suffix = [0] * (w+2)

for i in range(1, w+1):
    prefix[i] = max(prefix[i-1], arr[i-1])

for i in range(w, 0, -1):
    suffix[i] = max(suffix[i+1], arr[i-1])


water = 0
for i in range(1, w+1):
    water += min(prefix[i], suffix[i]) - arr[i - 1]

print(water) 