import sys
input = sys.stdin.readline


def find(x):
    if par[x] == x:
        return x
    else:
        x = find(par[x])
        par[x] = x
        return par[x]
    




g = int(input())
p = int(input())
par = [i for i in range(g+1)]

cnt = 0
plane = []
for _ in range(p):
    plane.append(int(input()))

for i in plane:
    k = find(i)
    if k == 0:
        break
    par[k] = k-1
    cnt += 1

print(cnt)