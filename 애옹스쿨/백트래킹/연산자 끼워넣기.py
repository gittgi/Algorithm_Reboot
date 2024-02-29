n = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))


max_val = -float("inf")
min_val = float("inf")
def recur(cur, val):
    global max_val, min_val
    if cur == n:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1

            if i == 0:
                recur(cur + 1, val + arr[cur])
            elif i == 1:
                recur(cur + 1, val - arr[cur])
            elif i == 2:
                recur(cur + 1, val * arr[cur])
            else:
                recur(cur + 1, val // arr[cur] if val > 0 else -(-val // arr[cur]))

            oper[i] += 1


recur(1, arr[0])

print(max_val) 
print(min_val)
