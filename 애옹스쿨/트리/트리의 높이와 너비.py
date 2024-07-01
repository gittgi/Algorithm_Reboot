import sys
sys.setrecursionlimit(10010)
input = sys.stdin.readline

n = int(input())

arr = [[0, 0] for _ in range(n+1)]
cnt_arr = [0 for i in range(10010)]


for _ in range(n):
    a, l, r = map(int, input().split())
    arr[a][0] = l
    arr[a][1] = r
    if l != -1:
        cnt_arr[l] = 1
    if r != -1:
        cnt_arr[r] = 1

root = -1
for i in range(1, len(cnt_arr)):
    if cnt_arr[i] == 0:
        root = i
        break

point = [[0, 0] for _ in range(n+1)]

x = 1
def dfs(cur, lv):
    global x
    l = arr[cur][0]
    r = arr[cur][1]
    # 왼쪽 먼저 순회
    if l != -1:
        dfs(l, lv + 1)
    
    # 이제 자기 자신
    point[cur][0] = lv
    point[cur][1] = x
    x += 1

    # 오른쪽 순회
    if r != -1:
        dfs(r, lv+1)

dfs(root, 1)

level = dict()

for i in range(1, n+1):
    lv, x = point[i]
    if lv in level:
        level[lv].append(x)
    else:
        level[lv] = [x]
max_val = 0
lv = 0
for i in level:
    val = max(level[i]) - min(level[i]) + 1
    if max_val < val:
        max_val = val
        lv = i
    elif max_val == val:
        if lv > i:
            lv = i

print(lv, max_val)



