n, target = map(int, input().split())

arr = list(map(int, input().split()))
arr += [0]

s = 0
e = 0
total = arr[0]

ans = float("inf")

while e < n:
    if total >= target:
        ans = min(ans, e - s + 1)
        total -= arr[s]
        s += 1
    else:
        e += 1
        total += arr[e]

if ans == float("inf"):
    print(0)
else:
    print(ans)