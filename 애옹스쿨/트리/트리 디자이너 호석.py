import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
ans = 0
# route[i] i 까지 가능한 경우의 수
route = [1 for i in range(n + 1)]
leaf_lst = []
# poss : 해당 레벨 까지 가능한 수열의 수
def dfs(x, prv, lst, poss):
    global ans
    cnt = 0
    for i in tree[x]:
        if i == prv:
            continue
        cnt += 1
        temp = 1
        for idx, val in lst:
            if val <= arr[i]:
                temp += route[idx]

        route[i] = temp
        lst.append((i, arr[i]))
        dfs(i, x, lst, poss + temp)
        lst.pop()
    
    if cnt == 0:
        leaf_lst.append(x)
        ans += poss



dfs(1, -1, [(1, arr[1])], 1)
print(ans % 1000000007)
        

