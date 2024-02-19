n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
arr = [0 for i in range(m)]
def recur(cur, start):
    if cur == m:
        print(*arr)
        return

    for i in range(start, n):
        arr[cur] = number[i]
        recur(cur+1, i+1)

recur(0, 0)

