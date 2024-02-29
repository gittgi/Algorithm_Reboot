n = int(input())
arr = [0]
for i in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))

benefit = 0
max_val = 0
# cur == 1부터 시작
def recur(cur):
    global benefit, max_val
    if cur > n+1:
        return
    else:
        max_val = max(max_val, benefit)
    
    for i in range(cur, n+1):
        t, p = arr[i]
        benefit += p
        recur(i + t) # i번째 일을 하는거니까 i 부터 t일 걸린 날 끝남
        benefit -= p

recur(1)
print(max_val)
