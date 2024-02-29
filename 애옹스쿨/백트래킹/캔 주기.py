n, k = map(int, input().split())
a = list(map(int, input().split()))
r = [list(map(int, input().split())) for _ in range(k)]
m = [list(map(int, input().split())) for _ in range(k)]

max_val = 0
val = 0
def recur(cur):
    global max_val, val
    if cur == k:
        max_val = max(val, max_val)
        return
    

    for i in range(n):
        if a[i] > 0:
            a[i] -= 1
            val += r[cur][i]
            for j in range(n):
                if a[j] > 0:
                    a[j] -= 1
                    val += m[cur][j]
                    recur(cur+1)
                    val -= m[cur][j]
                    a[j] += 1
            val -= r[cur][i]
            a[i] += 1
    

recur(0)
print(max_val)