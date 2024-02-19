n, k = map(int, input().split())
selected = []
ans = []

def rec(total):
    if total > n:
        return
    elif total == n:
        ans.append('+'.join(map(str, selected)))
    
    for i in range(1,4):
        selected.append(i)
        rec(total + i)
        selected.pop()


rec(0)
if len(ans) < k:
    print(-1)
else:
    print(sorted(ans)[k-1])