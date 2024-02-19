n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
arr = [0 for i in range(m)]

def recur(cur):
    if cur == m:
        print(*arr)
        return
    
    for i in range(n):
        arr[cur] = number[i]
        recur(cur + 1)

recur(0) 

