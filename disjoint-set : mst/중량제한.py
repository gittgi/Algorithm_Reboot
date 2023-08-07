import sys
input = sys.stdin.readline


n, m = map(int, input().split())

island = [i for i in range(n+1)]
length = [1 for i in range(n+1)]


def find(x):
    if x == island[x]:
        return x
    island[x] = find(island[x])
    return island[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if length[a] < length[b]:
        island[a] = b
        length[b] = max(length[b], length[a] + 1)

    else:
        island[b] = a
        length[a] = max(length[a], length[b] + 1)

arr = [0] * (m)

for i in range(m):
    a, b, d = map(int, input().split())
    arr[i] = (d, a, b)

arr.sort(reverse=True)

start, end = map(int, input().split())


for i in arr:
    d, a, b = i
    if find(a)!= find(b):
        union(a, b)
    if find(start) == find(end): # 크루스칼 하다가 둘이 연결된다 -> 내림차순이었기 때문에, 둘을 연결하는 가장 작은 값이 현재의 d 값
        print(d)
        quit()