n, k ,b = map(int, input().split())
arr = [True] * (n + 1)
arr += [False]
for _ in range(b):
    l = int(input())
    arr[l] = False

s = 1
e = k


broken = 0
for i in range(1, k + 1):
    if not arr[i]:
        broken += 1

ans = broken

while e < n+1:
    
    e += 1
    if not arr[e]:
        broken += 1
 
    if not arr[s]:
        broken -= 1
    s += 1

    ans = min(ans, broken)


print(ans)